##-----------------------------------------------------------------------------
##  Author      : Thuy Nguyen-Chinh
##  Date        : Nov 23, 2017
##
##  Interpreter : Python 3.5
##  Description : Verify an account
##-----------------------------------------------------------------------------


##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
from fnc.extractFeature import extractFeature
from fnc.matching import matching

from time import time
from sys import argv


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Parse argument
start = time()

filename = ''
if len(argv) == 2:
	filename = argv[1]
elif len(argv) == 1:
	id = 19
	group = 1
	temp = 3
	filename = 'im_db/%.3d_%d_%d' % (id, group, temp)


# Extract feature
print('>>> Start verifying {}...'.format(filename))
template, mask, filename = extractFeature(filename)


# Matching
id_acc = matching(template, mask, 0.40)

if id_acc == -1:
	print('>>> Error!')

elif id_acc == 0:
	print('>>> No matched!')

else:
	print('>>> ID {} is matched!'.format(str(id_acc)))


# Time measure
end = time()
print('>>> Verification time: {} [s]\n'.format(end - start))

