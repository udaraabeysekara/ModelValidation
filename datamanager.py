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

class Data_Manager:
  def __init__(self, filename, country = '', province_state = '', min_confirmed=0,min_deaths=0):
    ###Mandatory inputs
    self.filename = filename #Name of the input file
    self.country = country		#Name of the country as it is displayed in the file
    self.province_state = province_state
    self.min_confirmed  = min_confirmed
    self.min_deaths = min_deaths

    self.data = pd.read_csv(filename)
    self.data = self.data.replace(np.nan, 'NA', regex=True)

  def Set_Country(self, country):
    self.country = country

  def Set_Province_State(self, province_state):
    self.province_state = province_state

  def Set_Min_Confirmed():
    self.min_confirmed = min_confirmed

  def Set_Min_Deaths():
    self.min_deaths = min_deaths

  def Get_Total_Confirm(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0
    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    df = df.loc[df['Total_confirm'] != 'NA']
    return np.array(df.Date.values), np.array(df.Total_confirm.values)

    
  def Get_New_Confirm(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0

    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    df = df.loc[(df['new_confirm'] != 'NA')]
    return np.array(df.Date.values), np.array(df.new_confirm.values)


  def Get_Total_Death(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0

    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    df = df.loc[(df['Total_death'] != 'NA')]
    return np.array(df.Date.values), np.array(df.Total_death.values)


  def Get_New_Death(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0

    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    df = df.loc[(df['new_death'] != 'NA')]
    return np.array(df.Date.values), np.array(df.new_death.values)

  def Get_Population(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0

    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    if (len(np.array(df.PopTotal.unique())) > 1):
        print('Warning, more than one record for the total population found.')
    return np.array(df.PopTotal.unique())

  def Get_Pop_Density(self):
    if (self.country == ''):
      print('Error : Set the country using Set_Country()')
      return 0
    if (self.province_state == ''):
      print('Error : Set the province or state using Set_Country()')
      print('If there is no state set it to NA ')
      return 0
 
    df = self.data.loc[(self.data['Country_Region'] == self.country) & (self.data['Province_State'] == self.province_state)]
    if (len(np.array(df.PopDensity.unique())) > 1):
      print('Warning, more than one record for population density found.')
    return np.array(df.PopDensity.unique())

  def Get_Available_Countries(self):
  #Returns a numpy array of  available countries
    return np.array(self.data.Country_Region.unique())

  def Get_Province_State(self):
  #Returns a numpy array of all Province/State of a listed country.
  #If a country is not set it will generate an Warning
    if self.country == '':
      print('Warning !!!!!!!!!!!!!!')
      print('Country is not defined. Function is returning Province/State for all countries')
      state = np.array(self.data.Province_State.unique())
    else :
      country_data = self.data.loc[(self.data['Country_Region'] == self.country)]
      state = np.array(country_data.Province_State.unique())
    if len(state) <= 0:
      print('Warning !!!!!!!!')
      print('No States for the selecte country')
    return state

