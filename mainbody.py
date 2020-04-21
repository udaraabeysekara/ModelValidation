import numpy as np
import model  as MD #This is the importing the model clas
import DataAugmentation as DA
import evaluation as EV
import datamanager as DM 

##This part shows how to use the data manager to load new data and explore data
#Load data
test = DM.Data_Manager('C:\\Users\\u6026797\\Desktop\\COVID19_country_04-16-2020.csv')

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



#Generate a fake data set
#time   = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
#counts = np.array([0.0, 2.0, 4.0, 6.0,  8.0,  10.0])

#Lets do a fitting to a mode

#testmodel = MD.Model(time,counts,0,0,0,0)
#model_predicted_out = testmodel.linear_fit()

#Now evaluate the model output
#eval_test = EV.Model_Eval(time,counts,model_predicted_out)

#print(eval_test.Dummy_Chi_Square())

#Now lets do Data Augmentation
#DA_test = DA.Data_Augmentation(time,counts,np.array([0.0, 1.0]),0,0,0)
#Augmented_counts = DA_test.Gaussian_Augmentation()


#Do the fitting for the augmented data
#testAugmentation = MD.Model(time,Augmented_counts,0,0,0,0)
#aug_predict_out = testAugmentation.linear_fit()

#Evaluate the result after augmentation
#eval_augmentation = EV.Model_Eval(time,counts,aug_predict_out)
#print(eval_augmentation.Dummy_Chi_Square())


