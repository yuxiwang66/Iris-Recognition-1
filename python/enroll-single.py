##-----------------------------------------------------------------------------
##  Author      : Thuy Nguyen-Chinh
##  Date        : Nov 23, 2017
##
##  Interpreter : Python 3.5
##  Description : Enroll an account
##-----------------------------------------------------------------------------


##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
from fnc.extractFeature import extractFeature
from path import image_database_path, temp_database_path
from time import time
import scipy.io as sio
from sys import argv, exit
from os.path import exists


##-----------------------------------------------------------------------------
##  Function
##-----------------------------------------------------------------------------
def getIDFile(filename):
    """
    Description:
        Get ID string of the file name.

    Input:
        filename    - The input image file name.

    Output:
        id	        - The ID string corresponding to the file nam.
    """
    id = filename[-11:-8]
    id = int(id)
    id = str(id)
    return id


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Get the argument
if len(argv)==2:
	filename = '%s/%s' % (image_database_path, argv[1])
	if not exists(filename):
		print(">>> Wrong file!\n")
		exit()
elif len(argv)==1:
	filename = '%s001_1_1.jpg' % image_database_path
else:
	print(">>>Wrong syntax!\n")
	exit()

# Extract feature
print('>>> Enroll for the file ', filename)
start = time()
template, mask, filename = extractFeature(filename)
end = time()
print('>>> Enrollment time: {} [s]\n'.format(end-start))


# Save
sio.savemat('%s{}.mat'.format(getIDFile(filename)) % temp_database_path,
            mdict={'template':template, 'mask':mask})

