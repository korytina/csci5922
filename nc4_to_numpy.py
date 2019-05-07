# PURPOSE: Convert NetCDF4 file to Numpy .npy file
# EXAMPLE RUN (on server):
# module load python
# ncar_pylib
# cd ~dkorytin/deep_learning_class/
# python nc4_to_numpy.py

# changables
fin = 'pr_NAM-44_ECMWF-ERAINT_evaluation_r1i1p1_ISU-RegCM4_v4.4-rc8_day_20140101-20141231.nc'
fout = 'pr.npy'
var = 'pr'

# open input file
from netCDF4 import Dataset
dataset = Dataset(fin)
ny_in = len(dataset.dimensions['y'])
nx_in = len(dataset.dimensions['x'])
nt_in = len(dataset.dimensions['time'])
print ("ny_in,nx_in,nt_in = ", ny_in, nx_in, nt_in)

# save to nupy file
import numpy as np
a = dataset.variables[var][0:365, :, :]
print(a.shape)
np.save(fout, a.data)
d = np.load(fout)
a==d
print (d.shape)
