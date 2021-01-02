import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Parameter_data import *
#from Parameter_data import cross_section

#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/

x_list=np.arange(-30,30,0.1)
y_list=np.arange(-30,30,0.1)

print(np.corrcoef(x_list,y_list))