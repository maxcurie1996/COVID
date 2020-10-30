import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from Parameter_data import Gaussian
#from Parameter_data import cross_section

#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
def Gaussian(sigma,mu,x_list):
	return 1./(sigma * np.sqrt(2. * np.pi)) * np.exp( - (x_list - mu)**2. / (2. * sigma**2.) )

def norm_Gaussian(sigma,mu,x_list): #in quantum mech <psi 1| psi 1> = 1
	return 1./(np.pi**(1./4.) * np.sqrt(sigma)) * np.exp( - (x_list - mu)**2 / (2 * sigma**2) )
	
def cross_section(sigma1,mu1,sigma2,mu2):
	dx=0.01
	x_list=np.arange(-30,30,dx)
	return np.sum(norm_Gaussian(sigma1,mu1,x_list)*norm_Gaussian(sigma2,mu2,x_list)*dx)

x_list=np.arange(-10,10,0.01)

plt.clf()
plt.plot(x_list,Gaussian(1,0,x_list),label="location 0, mobility 1")
plt.plot(x_list,Gaussian(2,3,x_list),label="location 3, mobility 2")
plt.legend()
plt.show()

plt.clf()
plt.plot(x_list,Gaussian(1,0,x_list)*Gaussian(2,3,x_list),label="f1(x)*f2(x)")
plt.plot(x_list,Gaussian(1,0,x_list)*Gaussian(1,0,x_list),label="f1(x)*f1(x)")
plt.plot(x_list,Gaussian(1,0,x_list),label="location 0, mobility 1")
plt.plot(x_list,Gaussian(2,3,x_list),label="location 3, mobility 2")
plt.legend()
plt.show()

print(cross_section(1,0,2,3))
print(cross_section(1,0,1,0))