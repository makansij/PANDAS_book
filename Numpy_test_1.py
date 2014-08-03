__author__ = 'Jormak'

#In this file, I try out some stuff with numpy on the dataset that David gave me to work with.

# imports go here:
import numpy as np
import pandas as pd
import os

def get_to_correct_directory():
    while os.getcwd()!='C:\\Users\\Jormak':
        os.chdir(os.path.dirname(os.getcwd()))              #This moves up one level in directory
    os.chdir(os.getcwd()+'\\Downloads\\')  #This  moves us back down into the correct directory so that pandas will work

#grab the csv files
get_to_correct_directory()
Snow_Accumulation_data=pd.DataFrame.from_csv('SnowAccumulation.csv')
print 'Snow_Accumulation_data is of type \n', type(Snow_Accumulation_data)
print Snow_Accumulation_data




