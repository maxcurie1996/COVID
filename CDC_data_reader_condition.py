import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
#data from: 
#https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/data
path="C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/COVID/ga_covid_data/"
csvfile_name='comorbidities.csv'
data=pd.read_csv(path+csvfile_name)



#data["cdc_report_dt"] = data["cdc_report_dt"].astype("datetime64")

race_name_list=["Cardiovascular Disease","Any Chronic Condition","Chronic Liver Disease",\
"Chronic Lung Disease","Chronic Renal Disease",\
				"Currently Pregnant","Diabetes Mellitus",\
				"ICU","Immunocompromised Condition",\
				"Neurologic/Neurodevelopmental",\
				"Neurologic/Neurodevelopmental",\
				"Other Chronic Diseases",\
				"Smoker"
				]
#race_list=[0.5,2.5,7.5,13.5,23.5,34.5,44.5,54.5,64.5,74.5,84.5]

#print(len(age_name_list)-len(age_list))
#sys.exit()

death_count=[]
mild_count=[]
sever_count=[]
total_count=[]
percent=[]
print(str(data))
for i in range(len(race_name_list)):
	race_name=race_name_list[i]

	filt=(data['comorbidity']==race_name)
	data_temp=data[filt]
	#data_temp=data.loc[age_name,"death"]
	print(str(data_temp))
	temp=np.sum(data_temp['deaths'])

	print("*************")
	print(str(temp))
	print("*************")
	death_count.append(temp)
	
	temp=np.sum(data_temp['cases'])
	total_count.append(temp)

	temp=death_count[-1]/total_count[-1]
	percent.append(temp)


plt.clf()
#plt.plot(race_name_list,death_count,label="death")
#plt.plot(race_name_list,sever_count,label="sever")
#plt.plot(race_name_list,total_count,label="total")
plt.plot(race_name_list,percent)
#plt.legend()
plt.ylabel('death rate',fontsize=10)
#plt.xlabel('race',fontsize=10)
plt.title('COVID pre existing condition distribution')
plt.show()




