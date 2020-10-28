import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpi4py import MPI

#From: https://www.youtube.com/watch?v=13x90STvKnQ&list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi

comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

print('rank:'+str(rank))
print('node count:'+str(size))
print(str(9**(rank+3)))
