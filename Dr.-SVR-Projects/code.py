# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data, new_record),axis=0)
age = census[:, 0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print(round(max_age,2))
print(round(min_age,2))
print(round(age_mean))
print(round(age_std))

#Race distribution
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]

#length of the race arrays
len_0 = race_0.size
len_1 = race_1.size
len_2 = race_2.size
len_3 = race_3.size
minority_race = min(len_0,len_1,len_2,len_3)
print(minority_race)

#creating senior citizens
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(round(avg_working_hours,2))

#higher paying jobs
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
print(round(avg_pay_high,2))
print(round(avg_pay_low,2))





