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
import numpy as np
from fnc.boundary import searchInnerBound, searchOuterBound
from fnc.line import findline, linecoords
import multiprocessing as mp


##-----------------------------------------------------------------------------
##  Function
##-----------------------------------------------------------------------------
def segment(eyeim):
    """
	Description:
		Segment the iris region from the eye image.
		Indicate the noise region.

	Input:
		eyeim		- Eye image

	Output:
		ciriris		- Centre coordinates and radius of iris boundary.
		cirpupil	- Centre coordinates and radius of pupil boundary.
		imwithnoise	- Original image with location of noise marked with NaN.
	"""
    # Find the iris boundary by Daugman's intefro-differential
    rowp, colp, rp = searchInnerBound(eyeim)
    row, col, r = searchOuterBound(eyeim, rowp, colp, rp)

    # Package pupil and iris boundaries
    rowp = np.round(rowp).astype(int)
    colp = np.round(colp).astype(int)
    rp = np.round(rp).astype(int)
    row = np.round(row).astype(int)
    col = np.round(col).astype(int)
    r = np.round(r).astype(int)
    cirpupil = [rowp, colp, rp]
    ciriris = [row, col, r]

    # Find top and bottom eyelid
    imsz = eyeim.shape
    irl = np.round(row - r).astype(int)
    iru = np.round(row + r).astype(int)
    icl = np.round(col - r).astype(int)
    icu = np.round(col + r).astype(int)
    if irl < 0:
        irl = 0
    if icl < 0:
        icl = 0
    if iru >= imsz[0]:
        iru = imsz[0] - 1
    if icu >= imsz[1]:
        icu = imsz[1] - 1
    imageiris = eyeim[irl: iru + 1, icl: icu + 1]

    # Parallel computation
    ret_top = mp.Manager().dict()
    ret_bot = mp.Manager().dict()
    p_top = mp.Process(target=findTopEyelid,
                       args=(imsz, imageiris, irl, icl, rowp, rp, ret_top))
    p_bot = mp.Process(target=findBottomEyelid,
                       args=(imsz, imageiris, rowp, rp, irl, icl, ret_bot))
    p_top.start()
    p_bot.start()
    p_top.join()
    p_bot.join()
    mask_top = ret_top[0]
    mask_bot = ret_bot[0]

    # Mask the eye image, noise region is masked by NaN value
    imwithnoise = eyeim.astype(float)
    imwithnoise = imwithnoise + mask_top + mask_bot

    # For CASIA, eliminate eyelashes by threshold
    ref = eyeim < 80
    coords = np.where(ref == 1)
    imwithnoise[coords] = np.nan

    return ciriris, cirpupil, imwithnoise


#------------------------------------------------------------------------------
def findTopEyelid(imsz, imageiris, irl, icl, rowp, rp, ret_top):
    """
	Description:
		Mask for the top eyelid region.

	Input:
		imsz		- Size of the eye image.
		imageiris	- Image of the iris region.

		irl		    -
		icl		    -

		rowp		- y-coordinate of the inner circle centre.
		rp		    - radius of the inner circle centre.

	Output:
		mask    	- Map of noise that will be masked with NaN values.
	"""
    topeyelid = imageiris[0: rowp - irl - rp, :]
    lines = findline(topeyelid)
    mask = np.zeros(imsz, dtype=float)

    if lines.size > 0:
        xl, yl = linecoords(lines, topeyelid.shape)
        yl = np.round(yl + irl - 1).astype(int)
        xl = np.round(xl + icl - 1).astype(int)

        yla = np.max(yl)
        y2 = np.arange(yla)

        mask[yl, xl] = np.nan
        grid = np.meshgrid(y2, xl)
        mask[grid] = np.nan

    # Return
    ret_top[0] = mask
    return mask


#------------------------------------------------------------------------------
def findBottomEyelid(imsz, imageiris, rowp, rp, irl, icl, ret_bot):
    """
	Description:
		Mask for the bottom eyelid region.

	Input:
		imsz		- Eye image.
		imageiris	- Image of the iris region.

		rowp		- y-coordinate of the inner circle centre.
		rp		    - radius of the inner circle centre.

		irl		    -
		icl		    -

	Output:
		mask    	- Map of noise that will be masked with NaN values.
	"""
    bottomeyelid = imageiris[rowp - irl + rp - 1 : imageiris.shape[0], :]
    lines = findline(bottomeyelid)
    mask = np.zeros(imsz, dtype=float)

    if lines.size > 0:
        xl, yl = linecoords(lines, bottomeyelid.shape)
        yl = np.round(yl + rowp + rp - 3).astype(int)
        xl = np.round(xl + icl - 2).astype(int)
        yla = np.min(yl)
        y2 = np.arange(yla-1, imsz[0])

        mask[yl, xl] = np.nan
        grid = np.meshgrid(y2, xl)
        mask[grid] = np.nan

    # Return
    ret_bot[0] = mask
    return mask

