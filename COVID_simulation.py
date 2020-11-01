import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import imageio   #for making animation

from Parameter_data import data_set
from Parameter_data import Gaussian    		#/int Gauss dx=1
from Parameter_data import norm_Gaussian 	#<Gauss|Gauss>=1
from Parameter_data import cross_section
from Parameter_data import distance_calc

#https://youtu.be/gxAaO2rsdIs

total_human_num=5000
tot_steps=30
path='C:/Users/maxcu/OneDrive/Desktop/Documents/GitHub/Log_home/'

#simulaion infection of disease with relative realistic model 
class Human_info():
	def __init__(self):
		self.age = 0		# - female, + male
		self.location = [0,0]
		self.mobility = 0
		self.density = 0
		self.symptom = 4	# 0 dead
							# 1 recovered
							# 2 asymptomatic
							# 3 symptomatic
							# 4 no infected

		self.day = -1 # num days to recover/die
		self.tested=0	#1 if tested, 0 if not
		self.fear_factor=1 #how much people fear

def patient_zero():
	human_temp=Human_info()
	human_temp.age=25
	human_temp.location = [0,0]
	location,density=data_set("location")
	distance_list=distance_calc(location,human_temp.location)
	human_temp.density = density[np.argmin(distance_list)]
	human_temp.symptom=2
	human_temp.day=7
	human_temp.mobility=3.
	return human_temp


def age_list_generator(total_human_num):
	age,age_dis=data_set("age")
	age_dis = age_dis/np.sum(age_dis)
	age_list=np.random.choice(age, total_human_num, p=age_dis)
	return age_list


def location_list_generator(total_human_num):
	location,density=data_set("location")
	density = density/np.sum(density)
	location_index_list=np.random.choice(range(len(location)), total_human_num, p=density)
	location_list=[]
	density_list=[]
	for i in location_index_list:
		location_list.append(location[i])
		density_list.append(density[i])
	return location_list,density_list



def mobility_cal(human_info,total_human_num,stat):
	age_factor=(100.-(abs(human_info.age)-20.) )/80.    #100-distance from 30 years old(assume 30 years old is the most moble)
	if human_info.symptom==1 or human_info.symptom==2 or human_info.symptom==4: #recovered,asymptomatic,no infected
		sick_factor=1.
	if human_info.symptom==0: #dead
		sick_factor=0.
	elif human_info.symptom==3: #symptomatic
		sick_factor=0.2
	death_count=stat[0]
	get_COVID_count=stat[2]+stat[3]
	if (death_count>0.01*total_human_num and human_info.fear_factor==0) or\
	   (get_COVID_count>0.1*total_human_num and human_info.fear_factor==0):
		fear_factor = 10.
	elif human_info.fear_factor!=0 and human_info.fear_factor>=1:
		fear_factor = human_info.fear_factor*0.7 #fear decay
	elif human_info.fear_factor<1:
		fear_factor=1.
	else:
		fear_factor = human_info.fear_factor

	human_info.fear_factor=fear_factor
	density_factor = (human_info.density)**(-0.2)  #more denstiy, less movement
	mobility=age_factor*sick_factor*fear_factor**(-1.)*density_factor*0.01
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

def symptom_judge(human_info,Infect):
	if human_info.symptom==4: #not infected
		if Infect==1:
			age,age_dis=data_set("age")
			age_symptomatic_percent=data_set("symptom")
			age_index=np.argmin(abs(age-human_info.age))
			symptom=np.random.choice([2, 3], 1, p=[1-age_symptomatic_percent[age_index],\
													age_symptomatic_percent[age_index]])
			human_info.symptom=symptom
			sigma,mu = 2., 7.
			day_list=np.arange(1,15,1)
			human_info.day=np.random.choice(day_list, 1, p=Gaussian(sigma,mu,day_list)/np.sum(Gaussian(sigma,mu,day_list)))


	elif human_info.symptom==3:  	#symptomatic
		symptom=3
		day=human_info.day-1

		if day==0: 
			age,age_dis=data_set("age")
			age_index=np.argmin(abs(age-human_info.age))
			death_chance=data_set("death_recover")[age_index]
			dead_recover=np.random.choice([0,1], 1, p=[death_chance,1-death_chance])
			#print("dead_recover"+str(dead_recover))
			if dead_recover==1:
				symptom=1 #recovered
			elif dead_recover==0:
				symptom=0 #dead
		human_info.symptom=symptom
		human_info.day=day

	elif human_info.symptom==2:  	#asymptomatic
		symptom=2
		day=human_info.day-1
		if day==0: 
			symptom=1 #recovered
		human_info.symptom=symptom
		human_info.day=day
	


def Infection_calc(human_info0,human_list):
	[x0,y0]=human_info0.location
	r0=(x0**2.+y0**2.)**(0.5)
	mobility0=human_info0.mobility
	Infection_possibility=0   #can be greater than 1
	for human_info in human_list:
		if human_info.symptom==0 or human_info.symptom==1 or human_info.symptom==4: 
			continue
		else:
			[x,y]=human_info.location
			r=(x**2.+y**2.)**(0.5)
			print(str(mobility0)+", "+str(r0)+","+str(human_info.mobility)+","+str(r))
			cross_section_temp=cross_section(mobility0,r0,human_info.mobility,r)
			# \int Gaussian(sigma_1,mu_1,x)*Gaussian(sigma_2,mu_02,x) dx
			if human_info.symptom==3:
				Infection_possibility=Infection_possibility+cross_section_temp*0.5 	#Avoidance of syptomatic person
			elif human_info.symptom==2:
				Infection_possibility=Infection_possibility+cross_section_temp 		#Normal behavior
	#Infect=1 if infected, 0 if not
	age,age_dis=data_set("age")
	age_index=np.argmin(abs(age-human_info0.age))
	print("Infection_possibility"+str(Infection_possibility))
	infection_risk = 1-(data_set("infection_risk")[age_index])**Infection_possibility
	Infect=np.random.choice([0,1], 1, p=[1-infection_risk, infection_risk])
	return Infect
	

#a function of infection with uniform demagrafic
def human_list_generator(total_human_num):
	human_list=[]
	age_list=age_list_generator(total_human_num)
	location_list,density_list=location_list_generator(total_human_num)
	for i in range(total_human_num):
		human_temp=Human_info()
		human_temp.age = age_list[i]
		human_temp.location = location_list[i]
		human_temp.density=density_list[i]
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

def heat_map_pic(path,i,human_list):
	plt.clf()
	for human_info in human_list:
		[x,y]=human_info.location
		if human_info.symptom==1:
			plt.plot(x, y, marker='.', markersize=2, color='green',alpha=0.5)
		
	for human_info in human_list:
		[x,y]=human_info.location
		if human_info.symptom==0:
			plt.plot(x, y, marker='.', markersize=2, color='black',alpha=0.5)
		elif human_info.symptom==2:
			plt.plot(x, y, marker='.', markersize=2, color='orange',alpha=0.5)
		elif human_info.symptom==3:
			plt.plot(x, y, marker='.', markersize=2, color='red',alpha=0.5)
		elif human_info.symptom==4:
			plt.plot(x, y, marker='.', markersize=2, color='purple',alpha=0.5)


	plt.plot([0], [0], marker='.', markersize=2, color='black',label='dead')
	plt.plot([0], [0], marker='.', markersize=2, color='green',label='recovered')
	plt.plot([0], [0], marker='.', markersize=2, color='orange',label='asymptomatic')
	plt.plot([0], [0], marker='.', markersize=2, color='red',label='symptomatic')
	plt.plot([0], [0], marker='.', markersize=2, color='purple',label='no infected')

	plt.title("day"+str(i))
	plt.legend()
	plt.savefig(path+str(i)+'.png')
	#plt.show()

def simulation_main(total_human_num,tot_steps,path):
	csvfile_name=path+'COVID_sim_log.csv'

	with open(csvfile_name, 'w', newline='') as csvfile:
		COVID_data = csv.writer(csvfile, delimiter=',')
		COVID_data.writerow(['step','death','recover','asymptomatic','symptomatic','no_infected',\
			'tested_recover','tested_asymptom','tested_symptom','tested_no_infected'])
		csvfile.close()
	human_list=human_list_generator(total_human_num)
	human_list.append(patient_zero())
	ims_heat=[]
	for i in range(tot_steps):
		#*******start of logging the data*********
		stat=stat_calc(human_list)
		heat_map_pic(path,i,human_list)
		file_name=path+str(i)+'.png'
		ims_heat.append(imageio.imread(file_name))
		with open(csvfile_name, 'a+', newline='') as csvfile:
			COVID_data = csv.writer(csvfile, delimiter=',')
			COVID_data.writerow([i,stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],stat[6],stat[7],stat[8]])
			csvfile.close()	
		#*******end of logging the data*********
		for human_info in human_list:
			human_info.mobility=mobility_cal(human_info,total_human_num,stat)
			#****start of Infection***************
			if human_info.symptom==4:  #no infected
				Infect=Infection_calc(human_info,human_list)
			else:
				Infect=0
			symptom_judge(human_info,Infect)
			print('symptom, day='+str(human_info.symptom)+', '+str(human_info.day))
			#****End of of Infection***************
	
	imageio.mimwrite(path+'0dynamic_images.gif', ims_heat)
	plot_data(path)



simulation_main(total_human_num,tot_steps,path)
		
