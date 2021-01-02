import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#data from: 
#https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf/data
path="C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/Real_data/"
csvfile_name='COVID-19_Case_Surveillance_Public_Use_Data.csv'
data=pd.read_csv(path+csvfile_name)


#rename the column "cdc_report_dt" to "Time"
data=data.rename(columns={"cdc_report_dt":"Time"})
print("*********Rename**********")
print(data)

#slicing 
#data=data[0:3]
print("*********slicing**********")
print(data[0:3])
print(data.head(5))
print(data.tail(5))



print(data["Time"].is_unique) #see if the data has duplicates
print(data["Time"].value_counts())

#Set the index
data=data.set_index("Time")
data=data.set_index("County Name")
print("*********Set the index**********")
print(str(data))

#    	row 			col
print(data.loc["2020/06/24","icu_yn"])


#filter
filter=(data["State"]=="GA")
print( data[filter] )


#data["cdc_report_dt"] = data["cdc_report_dt"].astype("datetime64")

data['death_yn']=='No'#'Yes', 'Missing', 'Unknown', ''
filt=(data['death_yn']=='Yes')
death=data[filt]

#length=death["cdc_report_dt"].max()-death["cdc_report_dt"].min()

#print(length)

#a=np.histogram(death,bins=222)
#print(a)


