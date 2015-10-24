import numpy as np
import nibabel as ni
import pylab as plt

def compute_parcellations(functional, mask):
    functional = functional.reshape(( np.prod(functional.shape[0:3]), functional.shape[3] ))
    mask_vals = np.unique( mask )
    mask_vals = np.array([i for i in mask_vals if i > 0])
    avg_ts = np.zeros( ( mask_vals.shape[0] , functional.shape[1] ) )
    for i, r in enumerate(mask_vals):
        avg_ts[ i , : ] = np.mean( functional[ np.where( mask == r )[0] , : ] , 0 )
    return avg_ts


mask = ni.load('cc200.nii.gz').get_data()

print 'Mask loaded'

fmri = ni.load('all_runs.AMBAC002.nii')
data = fmri.get_data()

print 'fMRI loaded'

parcellated = compute_parcellations(data, mask)

plt.plot(parcellated[54])
plt.show()

print np.min(parcellated), np.max(parcellated)