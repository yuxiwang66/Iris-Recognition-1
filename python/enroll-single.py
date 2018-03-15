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
    id = filename[6:9]
    id = int(id)
    id = str(id)
    return id


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Extract feature
start = time()
filename = 'im_db/037_1_1'
template, mask, filename = extractFeature(filename)
end = time()
print('\n>>> Enrollment time: {} [s]\n'.format(end-start))


# Visualize
plt.figure(1)
plt.imshow(template, cmap='gray', interpolation='bicubic')
plt.show()


# Save
sio.savemat('acc_db/{}.mat'.format(getIDFile(filename)),
            mdict={'template':template, 'mask':mask})

