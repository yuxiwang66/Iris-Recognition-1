##-----------------------------------------------------------------------------
##  Author      : Chinh-Thuy Nguyen
##  Date        : Nov 11, 2017
##
##  Interpreter : 3.5
##  Editor      : Sublime Text 3
##-----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
from cv2 import imread

from fnc.segment import segment
from fnc.normalize import normalize
from fnc.encode import encode


##-----------------------------------------------------------------------------
##  Function
##-----------------------------------------------------------------------------
def extractFeature(im_filename):
	"""
	Description:
		Extract features from an iris image

	Input:
		im_filename	- The input iris image

	Output:
		template	- The extracted template
		mask		- The extracted mask
		im_filename	- The input iris image
	"""
	# Normalisation parameters
	radial_res = 20
	angular_res = 240

	# Feature encoding parameters
	minWaveLength = 18
	mult = 1
	sigmaOnf = 0.5

	# Perform segmentation
	im = imread(im_filename, 0)
	ciriris, cirpupil, imwithnoise = segment(im)

	# Perform normalization
	polar_array, noise_array = normalize(imwithnoise, ciriris[1], ciriris[0], ciriris[2],
										 cirpupil[1], cirpupil[0], cirpupil[2],
										 radial_res, angular_res)

	# Perform feature encoding
	template, mask = encode(polar_array, noise_array, minWaveLength, mult, sigmaOnf)

	# Return
	return template, mask, im_filename

