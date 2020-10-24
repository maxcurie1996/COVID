import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#https://youtu.be/gxAaO2rsdIs

#simulaion infection of disease with relative realistic model 
class Human_info():
	def __init__(self):
		self.age = 0
		self.gender = 0
		self.location = 0
		self.mobility = 0
		self.symptom = 0 # 0 recovered
						 # 1 asymptomatic
						 # 2 symptomatic
						 # 3 tested and infected
						 # 5 never get infected
		self.day = 0 # num days to recover
					 # -num days to die 

def age_list_generator(total_human_num):
	#age=int(np.arange(-90,90,5))
	age=np.arange(-87.5,90,5)
	print(age)
	female_dis=[9.57, 9.87, 10.18,10.31,10.57,11.5,11.08,10.85,10.01,10.31,10.39,11.23,10.71,9.26,7.53,5.33,3.64,4.23]
	male_dis=  [10.01,10.32,10.62,10.75,11.06,12,  11.35,10.88,9.91, 10.09,10.09,10.64,9.86, 8.2, 6.5, 4.32,2.68,2.38]
	age_dis = np.hstack((np.flip(female_dis), male_dis))
	age_dis = age_dis/np.sum(age_dis)
	temp=np.random.choice(age, total_human_num, p=age_dis)
	print(str(temp))

#a function of infection with uniform demagrafic
def human_list_generator(total_human_num):
	human_list=[]

	age_list_generator(total_human_num)
	for i in range(total_human_num):
		human_temp=Human_info()
		human_temp.age = 0
		human_temp.location = 0
		human_temp.mobility = 0
		human_temp.symptom = 0 
		human_temp.day = 5 

		human_list.append(human_temp)

human_list_generator(2)
