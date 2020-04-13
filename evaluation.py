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
class Model_Eval:
  def __init__(self, time, data_count, model_count):
    ###Mandatory inputs
    #time        -- the time time series, which is the independent variable of a model also known as x
    #data_count  -- the observed count in data
    #model_count -- the counts predicted by the model	

    self.time = time
    self.data_count = data_count
    self.model_count = model_count

#Each model returns the modified counts

#This function adds a Gaussian Noise to data and return the noise added counts array
#parameter[0] is the mean of the distribution
#parameter[1] is the standard divation

  def Dummy_Chi_Square(self):
     return np.mean((self.data_count - self.model_count)*(self.data_count - self.model_count))





