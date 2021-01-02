import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
#data from: 
#https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/data
path="C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/COVID/ga_covid_data/"
csvfile_name='demographics_by_age_group.csv'
data=pd.read_csv(path+csvfile_name)



#data["cdc_report_dt"] = data["cdc_report_dt"].astype("datetime64")

age_name_list=["<1 years","01-04 years","05-09 years","10-17 years","18-29 years",\
				"30-39 years","40-49 years","50-59 years","60-69 years", "70-79 years",\
				"80 & Older years"]
age_list=[0.5,2.5,7.5,13.5,23.5,34.5,44.5,54.5,64.5,74.5,84.5]

print(len(age_name_list)-len(age_list))
#sys.exit()

death_count=[]
mild_count=[]
sever_count=[]
total_count=[]
percent=[]
print(str(data))
for i in range(len(age_name_list)):
	age_name=age_name_list[i]
	age=age_list[i]
	filt=(data['age group']==age_name)
	data_temp=data[filt]
	#data_temp=data.loc[age_name,"death"]
	print(str(data_temp))
	temp=np.sum(data_temp['deaths'])

	print("*************")
	print(str(temp))
	print("*************")
	death_count.append(temp)
	
	temp1=np.sum(data_temp['hospitalization'])
	sever_count.append(temp1)
	temp=np.sum(data_temp['cases'])
	total_count.append(temp)
	temp2=temp-temp1
	mild_count.append(temp2)
	temp=death_count[-1]/total_count[-1]
	percent.append(temp)


plt.clf()
plt.plot(age_list,death_count,label="death")
plt.plot(age_list,sever_count,label="sever")
plt.plot(age_list,total_count,label="total")
#plt.plot(age_list,percent, label="mild")
#plt.legend()
plt.ylabel('death rate',fontsize=10)
plt.xlabel('Age',fontsize=10)
plt.title('COVID age distribution')
plt.show()




plt.clf()
plt.plot(age_list,death_count,label="death")
plt.plot(age_list,sever_count,label="sever")
plt.plot(age_list,total_count,label="total")
#plt.plot(age_list,percent, label="mild")
#plt.legend()
plt.ylabel('death rate',fontsize=10)
plt.xlabel('Age',fontsize=10)
plt.title('COVID age distribution')
plt.show()

