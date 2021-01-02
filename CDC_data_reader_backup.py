import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#data from: 
#https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/data
path="C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/COVID/ga_covid_data"
csvfile_name='demographics_by_age_group.csv'
data=pd.read_csv(path+csvfile_name)


#rename the column "cdc_report_dt" to "Time"
data=data.rename(columns={"cdc_report_dt":"Time"})
print("*********Rename**********")
print(data)

#slicing 
#data=data[0:3]
print("*********slicing**********")
print(data[0:3])




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
death["Time"].hist(bins=222)
print()
print(np.shape(np.array(death["Time"].hist(bins=222))))
#plt.legend()
plt.ylabel('count',fontsize=10)
plt.xlabel('Time',fontsize=10)
plt.title('COVID data')
#plt.savefig('COVID.png')
plt.show()

print(str(set(data["Time"])))
date_list=list(set(data["Time"])).sort()
#for i in range(len(date_list)):
#	date_list=

print(str(date_list))

