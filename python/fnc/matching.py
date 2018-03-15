##-----------------------------------------------------------------------------
##  Author      : Chinh-Thuy Nguyen
##  Date        : Nov 24, 2017
##
##  Interpreter : Python 3.5
##  Description	: Verify the correspondence between the input template with
##				  templates in the database.
##-----------------------------------------------------------------------------


##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import numpy as np
from os import listdir
from fnmatch import filter
import scipy.io as sio
from multiprocessing import Pool
from itertools import repeat


##-----------------------------------------------------------------------------
##  Function
##-----------------------------------------------------------------------------
def matching(template_extr, mask_extr, threshold):
	"""
	Description:
		Match the extracted template with database.

	Input:
		template_extr	- Extracted template.
		mask_extr		- Extracted mask.
		threshold		- Threshold of distance.

	Output:
		id_acc			- ID of the matched account, 0 if not, -1 if error.
	"""
	# Get the number of accounts in the database
	numfile = len(filter(listdir('acc_db/'), '*.mat'))
	if numfile == 0:
		id_acc = -1
		return id_acc

	# Parallel computation: Calculate the Hamming distance
	args = zip(range(numfile), repeat(template_extr), repeat(mask_extr))
	with Pool(processes=4) as pool:
		hm_dist = pool.starmap(matchingPool, args)

	# Threshold and give the result ID
	hm_dist = np.array(hm_dist)
	id_acc = np.where(hm_dist <= threshold)		# default=0.38
	if len(id_acc[0]) < 1:
		id_acc = 0
		return id_acc
	elif len(id_acc[0]) > 1:
		id_acc = -1
		return id_acc

	# Return
	return id_acc[0][0]+1


#------------------------------------------------------------------------------
def calHammingDist(template1, mask1, template2, mask2):
	"""
	Description:
		Calculate the Hamming distance between two iris templates.

	Input:
		template1	- The first template.
		mask1		- The first noise mask.
		template2	- The second template.
		mask2		- The second noise mask.

	Output:
		hd			- The Hamming distance as a ratio.
	"""
	# Initialize
	hd = np.nan

	# Shift template left and right, use the lowest Hamming distance
	for shifts in range(-8,9):
		template1s = shiftbits(template1, shifts)
		mask1s = shiftbits(mask1, shifts)

		mask = np.logical_or(mask1s, mask2)
		nummaskbits = np.sum(mask == 1)
		totalbits = template1s.size - nummaskbits

		C = np.logical_xor(template1s, template2)
		C = np.logical_and(C, np.logical_not(mask))
		bitsdiff = np.sum(C==1)

		if totalbits == 0:
			hd = np.nan
		else:
			hd1 = bitsdiff / totalbits
			if hd1 < hd or np.isnan(hd):
				hd = hd1

	# Return
	return hd


#------------------------------------------------------------------------------
def shiftbits(template, noshifts):
	"""
	Description:
		Shift the bit-wise iris patterns.

	Input:
		template	- The template to be shifted.
		noshifts	- The number of shift operators, positive for right
					  direction and negative for left direction.

	Output:
		templatenew	- The shifted template.
	"""
	# Initialize
	templatenew = np.zeros(template.shape)
	width = template.shape[1]
	s = 2 * np.abs(noshifts)
	p = width - s

	# Shift
	if noshifts == 0:
		templatenew = template

	elif noshifts < 0:
		x = np.arange(p)
		templatenew[:, x] = template[:, s + x]
		x = np.arange(p, width)
		templatenew[:, x] = template[:, x - p]

	else:
		x = np.arange(s, width)
		templatenew[:, x] = template[:, x - s]
		x = np.arange(s)
		templatenew[:, x] = template[:, p + x]

	# Return
	return templatenew


#------------------------------------------------------------------------------
def matchingPool(id, template_extr, mask_extr):
	"""
	Description:
		Perform matching session within a Pool of parallel computation

	Input:
		id				- ID of the examining template
		template_extr	- Extracted template
		mask_extr		- Extracted mask of noise

	Output:
		hm_dist			- Hamming distance
	"""
	# Load each account
	data_template = sio.loadmat('acc_db/{}.mat'.format(str(id+1)))
	template = data_template['template']
	mask = data_template['mask']

	# Calculate the Hamming distance
	hm_dist = calHammingDist(template_extr, mask_extr, template, mask)
	return hm_dist

