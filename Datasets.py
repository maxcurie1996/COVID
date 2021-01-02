import io
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('income_cases_2.csv')


norm_death=df["deaths"]/df["Total_Population"]
norm_low=df["HH_income_less_35k_MOE"]/df["Total_Population"]
temp=np.argmax(norm_death)

print(temp)
print(norm_low[temp])
print(norm_death[temp])
print(df["deaths"][temp])
print(df["HH_income_less_35k_MOE"][temp])
print(df["Total_Population"][temp])



plt.clf()
plt.plot(norm_low,norm_death,"o",markersize=1)
plt.show()


correlate=np.corrcoef(norm_death,norm_low)
print(correlate)
