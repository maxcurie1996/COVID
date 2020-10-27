import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
def Gaussian(sigma,mu,x_list):
	return 1./(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x_list - mu)**2 / (2 * sigma**2) )

r_boundary=30. #30 miles boundary
sigma=2.       #2  miles radius city center
mu=0    #[0,0] is the city center

#From https://stackoverflow.com/questions/32208359/is-there-a-multi-dimensional-version-of-arange-linspace-in-numpy
xy = np.mgrid[-r_boundary:r_boundary:1, -r_boundary:r_boundary:1].reshape(2,-1).T #even spaced grid in cartesian coordinates

location=[]
density=[]

for coord in xy:
	[x, y]=coord
	r=(x**2.+y**2.)**(0.5)
	if r<=r_boundary:  #with in the boundary
		location.append([x, y])
		#print(r)
		#print(Gaussian(sigma,mu,r))
		density.append(Gaussian(sigma,mu,r))

print(str(location))
print(str(density))