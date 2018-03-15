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
from path import image_database_path, temp_database_path


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Prepare
id = 20
group = 2
temp = 4
filename = '%s%.3d_%d_%d.jpg' % (image_database_path ,id, group, temp)


# Extract feature
start = time()
print('>>> Start verifying {}...'.format(filename))
template, mask, filename = extractFeature(filename)


# Matching
id_acc = matching(template, mask, 0.42)

if id_acc == -1:
	print('>>> Error!')

elif id_acc == 0:
	print('>>> No matched!')

else:
	print('>>> ID {} is matched!'.format(str(id_acc)))


# Time measure
end = time()
print('>>> Verification time: {} [s]\n'.format(end - start))

