# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:36:49 2020

@author: u6026797
"""

#%% Call in libraries
import os 
os.chdir('/Users/u6026797/Documents/GitHub/ModelValidation/')

import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from matplotlib import pyplot as plt
import datetime as dt

import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.optimizers import SGD 
from keras.callbacks import EarlyStopping
from keras.utils import np_utils
import itertools
from keras.layers import LSTM
from keras.layers import Dropout

import DataAugmentation as DA
import evaluation as EV
import datamanager as DM 

#%% Import data
#set location of source file
covid_data = DM.Data_Manager('/Users/u6026797/Desktop/COVID19_country_04-21-2020.csv')
country_array = covid_data.Get_Available_Countries()

#set as pd.df as needed
#covid_data.Set_Country('Belgium')
#covid_data.Set_Province_State('NA')
#date, new_confirm = covid_data.Get_New_Confirm()
#test_df = pd.DataFrame({'new_confirm':new_counts,
#                       'date':date})
#test_df_index = test_df.set_index('date')

#%% Create transformation augmentation loop
#create output df
best_trans_df = pd.DataFrame({'Country','Region','Avg_Scaled_Error',
              'Transformation','Augmentation'})
#for country
for country in country_array:
    covid_data.Set_Country(country)
    prov_array = test.Get_Province_State
    for region in prov_array:

x = DA.Data_Augmentation(time=date,count=new_confirm,parameter=1,minimum=1,maximum=1,units=1)
x.Percent_Increase()


#%% Create model hyperparameter validation loop
best_param_df = pd.DataFrame({'Country','Avg_Scaled_Error',
              'Param1','...','ParamN'})

#%% Plots        