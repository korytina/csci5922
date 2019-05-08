# csci5922
class project: superresolution from low-res percipitation data over North America

This project aims to deploy a GAN model to upscale low resolution daily precipitation simulations over North America to a high resolution, specifically 4x in both x and y dimensions.

Contents
pr.npy.zip 	sole data file: zipped numpy .npy, remember to unzip! 

baseline.ipynb 	
  - requires pr.npy for be in ./ run with python3 	
baseline.py 	
  - to run: 
     1) unzip the zip file
     2) python3 baseline.py 	

final_slides.pdf 	
project_report.pdf 

nc4_to_numpy.py 	Converts NetCDF4 file to .npy 
		
srgan_pr.ipynb 	Vanilla GAN customized for 50km pr prediction. Based on medium dot co… 	
utils.py 	helper file for Logger() from medium dot com 
