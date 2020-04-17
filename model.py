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
from scipy.optimize import curve_fit

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
    #self.model_func(initial_parameter, initial_parameter, initial_parameter)

#This is a simple model just for testing. Should not be used for real modelng.
  def model_func(self, x, Ro,alpha):
    y_return = [Ro]
    for x_val in x[1:]:
      y = [Ro]
      for i in range(1,int(x_val)):
        y.append(y[-1]+Ro*np.power(alpha,i))
      y_return.append(y[-1])
    return y_return

  def Fake_SIR_Model(self):
    popt, pcov = curve_fit(self.model_func, self.time, self.count)
    y_modeled = self.model_func(self.time ,popt[0],popt[1])
    y_err_up = self.model_func(self.time ,popt[0]+pcov[0,0]**0.5,popt[1]+pcov[1,1]**0.5)
    y_err_down = self.model_func(self.time ,popt[0]-pcov[0,0]**0.5,popt[1]-pcov[1,1]**0.5)
    return y_modeled, y_err_down, y_err_up


