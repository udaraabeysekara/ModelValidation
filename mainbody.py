import numpy as np
import model  as MD #This is the importing the model clas
import DataAugmentation as DA
import evaluation as EV


#Generate a fake data set
time   = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
counts = np.array([0.0, 2.0, 4.0, 6.0,  8.0,  10.0])

#Lets do a fitting to a mode

testmodel = MD.Model(time,counts,0,0,0,0)
model_predicted_out = testmodel.linear_fit()

#Now evaluate the model output
eval_test = EV.Model_Eval(time,counts,model_predicted_out)

print(eval_test.Dummy_Chi_Square())

#Now lets do Data Augmentation
DA_test = DA.Data_Augmentation(time,counts,np.array([0.0, 1.0]),0,0,0)
Augmented_counts = DA_test.Gaussian_Augmentation()


#Do the fitting for the augmented data
testAugmentation = MD.Model(time,Augmented_counts,0,0,0,0)
aug_predict_out = testAugmentation.linear_fit()

#Evaluate the result after augmentation
eval_augmentation = EV.Model_Eval(time,counts,aug_predict_out)
print(eval_augmentation.Dummy_Chi_Square())


