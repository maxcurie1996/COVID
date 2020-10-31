import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Parameter_data import *
#from Parameter_data import cross_section

#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/

x_list=np.arange(-30,30,0.1)
a=np.sum(norm_Gaussian(1.,0.,x_list)*norm_Gaussian(1.,0.,x_list)*0.1)
print(a)
b=cross_section(1,0,1,0)
print(b)