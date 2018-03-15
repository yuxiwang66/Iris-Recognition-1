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
from matplotlib import pyplot as plt
from time import time
import scipy.io as sio


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
# Extract feature
start = time()
filename = '%s/019_1_1.jpg' % image_database_path
template, mask, filename = extractFeature(filename)
end = time()
print('\n>>> Enrollment time: {} [s]\n'.format(end-start))


# Visualize
plt.figure(1)
plt.imshow(template, cmap='gray', interpolation='bicubic')
plt.show()


# Save
sio.savemat('%s{}.mat'.format(getIDFile(filename)) % temp_database_path,
            mdict={'template':template, 'mask':mask})

