#
#
#

#variable naming conventions
#1) Every class or function first letter of each word is capital
#2) For variables do not use capital letters
#3) If there are more than one word seperate them by _ 
#4) For clases and functions first letter of each word is capital
#4) Reference to the current instance of the class allways should be self
#5) Each class and function should have an explanation

import numpy as np
import pandas as pd
class Data_Augmentation:
  def __init__(self, time, count, parameter, minimum, maximum,units):
    ###Mandatory inputs
    #time  -- the time time series, which is the independent variable of a model also known as x
    #count -- the observed count in each time bin, which is the dependent variable
    ###Optional inputs 
    #parameter 		-- Some Augmentation method require to pass parameters
    #minimum           	-- Optional may be required in the future
    #maximum           	-- Optional may be required in the future
    #units             	-- Optional may be required in the future
    self.time = time
    self.count = count
    self.parameter = parameter
    self.minimum = minimum
    self.maximum = maximum
    self.units = units

#Each model returns the modified counts

#This function adds a Gaussian Noise to data and return the noise added counts array
#parameter[0] is the mean of the distribution
#parameter[1] is the standard divation

  def Gaussian_Augmentation(self):
     noise = np.random.normal(self.parameter[0], self.parameter[1], self.time.size)	       
     return self.count+noise
 
  def Percent_Increase(self):
    output = [0]
    for steps in range(len(self.count)-1):
        if steps<len(self.count):
            denom = self.count[steps]
            if denom==0:
                denom=1
            output.append(self.count[steps+1]/denom)
    return np.array(output)

  def Estimate_Derivative(self):
      return np.diff(self.count,prepend=[0])
  
  def Resample(self,date_format='%Y-%m-%d',resample_dir='up'):
    '''
    Resamples the input array to scalar length (.5 or 2). Takes two arguments: 
          1. Source date format, ie: '%Y-%m-%d'
          2. Target resample scalar, ie: up=2, down=.5.
    Nans induced by upsampling are filled with linear interpolation, downsamples are returned as sums
    Returns new time and count indexes as np.arrays
    '''
    temp_df = pd.DataFrame({'count':self.count,
                           'time':self.time})
    temp_df['time'] = pd.to_datetime(temp_df['time'], format=date_format)
    temp_df = temp_df.set_index('time')
    if resample_dir == 'up':
      temp_df=temp_df.resample('12H').asfreq()
      temp_df['count']=temp_df['count'].astype(float)
      temp_df['count']=temp_df['count'].interpolate(method='linear')
      return [np.array(temp_df['count']),np.array(temp_df.index)]
    elif resample_dir == 'down':
      temp_df=temp_df.resample('2D').sum()  
      return [np.array(temp_df['count']),np.array(temp_df.index)]
      
