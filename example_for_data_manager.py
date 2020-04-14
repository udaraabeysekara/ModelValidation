import numpy as np
import model  as MD #This is the importing the model clas
import DataAugmentation as DA
import evaluation as EV
import datamanager as DM 

##This part shows how to use the data manager to load new data and explore data
#Load data
test = DM.Data_Manager('/Users/u0979082/Documents/COVID19Research/Evan_Dataset_Code_scrubbed/COVID19_country_04-02-2020.csv')

#Lets Look at the available countries
print(test.Get_Available_Countries())

#France is available lets set the country to France
test.Set_Country('France')

#Now Look at available State
print(test.Get_Province_State())

#Province Main is available. Lets look at the Main
test.Set_Province_State('Main')

#Lets look at available data
#Population density
print(test.Get_Pop_Density())
#Total population
print(test.Get_Pupulation())

#Now you can pull data in different formats. 
#All outputs are two numpy arrays, time and counts
#Note that all empty elements are removed. 

New_Death_Time, New_Death_Count = test.Get_New_Death()
#Now you can pass them to a model data augmentation, what every you want to do with data
#I am printing here
print(New_Death_Time)
print(New_Death_Count)

#Same thing here for all the other methods
Total_Conf_Death_Time, Total_Conf_New_Death_Count = test.Get_Total_Confirm()

New_Conf_Time, New_Conf_Count = test.Get_New_Confirm()

Total_Death_Time, Total_Death_Count = test.Get_Total_Death()



#Ignore the warning /usr/local/lib/python3.6/site-packages/pandas/core/ops/__init__.py:1115: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison  result = method(y)

#It is a warning that I could correct I will correct it later. There is no harm for your data here
