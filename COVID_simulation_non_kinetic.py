import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

#https://youtu.be/gxAaO2rsdIs

total_human_num=4000
tot_steps=200
path='C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/Log/'

#simulaion infection of disease with relative realistic model 
class Human_info():
	def __init__(self):
		self.age = 0
		self.gender = 0
		self.location = [0,0]
		self.mobility = 0
		self.density = 0
		self.symptom = 4    
							# 0 dead
							# 1 recovered
							# 2 asymptomatic
							# 3 symptomatic
							# 4 no infected

		self.day = -1 # num days to recover/die
		self.tested=0	#1 if tested, 0 if not

def age_list_generator(total_human_num):
	#age=int(np.arange(-90,90,5))
	age=np.arange(-87.5,90,5)
	#print(age)
	#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/
	female_dis=[9.57, 9.87, 10.18,10.31,10.57,11.5,11.08,10.85,10.01,10.31,10.39,11.23,10.71,9.26,7.53,5.33,3.64,4.23]
	male_dis=  [10.01,10.32,10.62,10.75,11.06,12,  11.35,10.88,9.91, 10.09,10.09,10.64,9.86, 8.2, 6.5, 4.32,2.68,2.38]
	age_dis = np.hstack((np.flip(female_dis), male_dis))
	age_dis = age_dis/np.sum(age_dis)
	age_list=np.random.choice(age, total_human_num, p=age_dis)
	return age_list



def mobility_cal(human_info,stat):

	age_factor=100-(abs(human_info.age)-20)    #100-distance from 30 years old(assume 30 years old is the most moble)
	if human_info.symptom==6:
		sick_factor=100
	if human_info.symptom==0 or human_info.symptom==1 or human_info.symptom==5:
		sick_factor=80
	elif human_info.symptom==2 or human_info.symptom==3:
		sick_factor=20
	fear_factor= death_rate
	density_factor = (human_info.density)**(-1)  #more denstiy, less movement
	mobility=age_factor*sick_factor*(1.-fear_factor)*density_factor
	return mobility

def stat_calc(human_list):
	stat=[]
	death_count=0         	# 0 dead

	recover_count=0			# 1 recovered
	asymptomatic_count=0	# 2 asymptomatic
	symptomatic_count=0		# 3 symptomatic
	no_infected=0			# 4 no infected

	tested_recover=0		# 5 tested and recovered
	tested_asymptom=0		# 6 tested and asymptom
	tested_symptom=0		# 7 tested and symptom
	tested_no_infected=0	# 8 tested and no infected
	
	
	for human_info in human_list:
		if human_info.symptom==0:
			death_count=death_count+1
		elif human_info.symptom==1:
			recover_count=recover_count+1
		elif human_info.symptom==2:
			asymptomatic_count=asymptomatic_count+1
		elif human_info.symptom==3:
			symptomatic_count=symptomatic_count+1
		elif human_info.symptom==4:
			no_infected=no_infected+1

		elif human_info.symptom==1 and human_info.tested==1:
			tested_recover=tested_recover+1
		elif human_info.symptom==2 and human_info.tested==1:
			tested_asymptom=tested_asymptom+1
		elif human_info.symptom==3 and human_info.tested==1:
			tested_symptom=tested_symptom+1
		elif human_info.symptom==4 and human_info.tested==1:
			tested_no_infected=tested_no_infected+1

		
	stat.append(death_count)
	stat.append(recover_count)
	stat.append(asymptomatic_count)
	stat.append(symptomatic_count)
	stat.append(no_infected)
	stat.append(tested_recover)
	stat.append(tested_asymptom)
	stat.append(tested_symptom)
	stat.append(tested_no_infected)
	return stat

def moving(human_info):
	return coord

def symptom_judge(human_info):
	if human_info.symptom==4: 
		age=np.arange(-87.5,90,5)
		
		age_asymptomatic_percent=[0.08]*len(age) 	# 2 asymptomatic
		age_symptomatic_percent=[0.05]*len(age)  	# 3 symptomatic
													# 4 never get infected
		age_index=np.argmin(abs(age-human_info.age))


		symptom=np.random.choice([2, 3, 4], 1, p=[age_asymptomatic_percent[age_index],\
													age_symptomatic_percent[age_index],
													(1.	-age_asymptomatic_percent[age_index]\
											   		-age_symptomatic_percent[age_index])])
		if symptom!=4:
			day=7
		else: 
			day=-1
	elif human_info.symptom==3:  	#symptomatic
		symptom=3
		day=human_info.day-1

		if day==0: 
			dead_recover=np.random.choice([0,1], 1, p=[0.01,0.99])
			#print("dead_recover"+str(dead_recover))
			if dead_recover==1:
				symptom=1 #recovered
			elif dead_recover==0:
				symptom=0 #dead

	elif human_info.symptom==2:  	#asymptomatic
		symptom=2
		day=human_info.day-1
		if day==0: 
			symptom=1 #recovered
	else:
		symptom=human_info.symptom
		day=human_info.day
			
	return symptom, day

#a function of infection with uniform demagrafic
def human_list_generator(total_human_num):
	human_list=[]

	age_list=age_list_generator(total_human_num)

	for i in range(total_human_num):
		human_temp=Human_info()
		human_temp.age = age_list[i]
		human_temp.location = 0
		human_list.append(human_temp)

	return human_list

def plot_data(path):
	csvfile_name=path+'COVID_sim_log.csv'
	data=pd.read_csv(csvfile_name)

	plt.clf()
	plt.plot(data['step'],data['death'], label='death')
	plt.plot(data['step'],data['recover'], label='recover')
	plt.plot(data['step'],data['asymptomatic'], label='asymptomatic')
	plt.plot(data['step'],data['symptomatic'], label='symptomatic')
	plt.plot(data['step'],data['no_infected'], label='no_infected')
	plt.legend()
	plt.show()

	plt.clf()
	plt.plot(data['step'],data['tested_recover'], label='tested_recover')
	plt.plot(data['step'],data['tested_asymptom'], label='tested_asymptom')
	plt.plot(data['step'],data['tested_symptom'], label='tested_symptom')
	plt.plot(data['step'],data['tested_no_infected'], label='tested_no_infected')
	plt.legend()
	plt.show()

def simulation_main(total_human_num,tot_steps,path):
	csvfile_name=path+'COVID_sim_log.csv'

	with open(csvfile_name, 'w', newline='') as csvfile:
		COVID_data = csv.writer(csvfile, delimiter=',')
		COVID_data.writerow(['step','death','recover','asymptomatic','symptomatic','no_infected',\
			'tested_recover','tested_asymptom','tested_symptom','tested_no_infected'])
		csvfile.close()

	human_list=human_list_generator(total_human_num)
	for i in range(tot_steps):
		#*******start of logging the data*********
		stat=stat_calc(human_list)
		with open(csvfile_name, 'a+', newline='') as csvfile:
			COVID_data = csv.writer(csvfile, delimiter=',')
			COVID_data.writerow([i,stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],stat[6],stat[7],stat[8]])
			csvfile.close()	
		#*******end of logging the data*********
		for human_info in human_list:
			print('symptom, day='+str(human_info.symptom)+', '+str(human_info.day))
			symptom_temp, day_temp=symptom_judge(human_info)
			#print('symptom_temp, day_temp='+str(symptom_temp)+', '+str(day_temp))
			human_info.symptom=symptom_temp
			human_info.day=day_temp

	plot_data(path)


simulation_main(total_human_num,tot_steps,path)
		
