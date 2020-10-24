import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#data from: 
#https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/data

csvfile_name='COVID-19_Case_Surveillance_Public_Use_Data.csv'
data=pd.read_csv(csvfile_name)


#data["cdc_report_dt"] = data["cdc_report_dt"].astype("datetime64")

data['death_yn']=='No'#'Yes', 'Missing', 'Unknown', ''
filt=(data['death_yn']=='Yes')
death=data[filt]

#length=death["cdc_report_dt"].max()-death["cdc_report_dt"].min()

#print(length)

#a=np.histogram(death,bins=222)
#print(a)

plt.clf()
#plt.plot(death(2), label='Price')
death["cdc_report_dt"].hist(bins=222)
print()
print(np.shape(array(death["cdc_report_dt"].hist(bins=222))))
plt.legend()
plt.ylabel('count',fontsize=10)
plt.xlabel('Time',fontsize=10)
plt.title('COVID data')
#plt.savefig('COVID.png')
plt.show()