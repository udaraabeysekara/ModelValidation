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
class Model:
  def __init__(self, time, count, initial_parameter, minimum, maximum, units):
    ###Mandatory inputs
    #time  -- the time time series, which is the independent variable of a model also known as x
    #count -- the observed count in each time bin, which is the dependent variable
    ###Optional inputs 
    #initial_parameter -- Some models require an initial set of parameter
    #minimum           -- Optional may be required in the future
    #maximum           -- Optional may be required in the future
    #units             -- Optional may be required in the future
    self.time = time
    self.count = count
    self.minimum = minimum
    self.maximum = maximum
    self.units = units

#This is a fake model that fits a linear function between x=time and y=count
#The function returns an array with the model output y_hat
#We have to add a function per every model
  def linear_fit(self):
    m,c = np.polyfit(self.time, self.count, 1)   
    return m*self.time + c


