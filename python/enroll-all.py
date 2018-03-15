##-----------------------------------------------------------------------------
##  Author      : Thuy Nguyen-Chinh
##  Date        : Nov 27, 2017
##
##  Interpreter : Python 3.5
##  Description : Enroll accounts for the whole of database
##-----------------------------------------------------------------------------


##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
from fnc.extractFeature import extractFeature
from path import image_database_path, temp_database_path
from time import time
import scipy.io as sio


##-----------------------------------------------------------------------------
##  Function
##-----------------------------------------------------------------------------
def getIDFile(filename):
    id = filename[-11:-8]
    id = int(id)
    id = str(id)
    return id


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
start = time()
for i in range(108):
    template, mask, filename = extractFeature('%s%.3d_%d_%d.jpg' 	\
    									% (image_database_path ,i+1, 1, 1))
    sio.savemat('%s{}.mat'.format(getIDFile(filename)) % temp_database_path, 
                mdict={'template': template, 'mask': mask})
    print(filename)
end = time()
print('\n>>> Enrollment time: {} [s]\n'.format(end-start))

