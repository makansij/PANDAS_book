__author__ = 'Jormak'

'''
Goals :
    1.  Create a bar graph of 5 most common names for a single year
        - one for Males
        - one for Females
    2.  Create a line graph of number of occurrences (y axis), throughout time (x axis) for the following names, for each gender:

        - Lisa -- Male and Female
        - Jordan -- etc., you get the point
        - Eric\Erick\Erik
        - Cole
        - Gabriel\Gabe\Gabby\Gabrielle

    Remember you have to do MALE and FEMALE for each one of those

'''

#List of imports

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
import os

# Here I will tackle the first goal

def main():
    year=input('Please input the year for which you would like to know the 5 most common names')
    dFrame = open_file('yob'+str(year)+'.txt') #Data is a list.  Each element in "Data" is a column of data
    # the "groupby()" method creates an iterable object (however for some reason you can't index it).  Look here:
    Females, Males = top_5_each_sex(dFrame)  # this spits back two DataFrames
    create_plots(Females, Males, year)  # this plots the Females and Males

def open_file(file_name):
    ''' file_name should be a string.
    this function navigates to the correct directory and opens a file of name file_name.
    It returns the file as a csv. '''
    current_directory=os.getcwd()
    if current_directory!='C:\\Users\\Jormak\\PycharmProjects\\PANDAS_Book\\pydata-book\\ch02\\names':
        os.chdir('C:\\Users\\Jormak\\PycharmProjects\\PANDAS_Book\\pydata-book\\ch02\\names')
    Data = pd.read_csv(file_name, names=['name', 'sex', 'births'])   #check out how this works.  This is really powerful.
    return Data

def top_5_each_sex(dFrame):
    '''  dFrame is a DataFrame.  This function returns two dataframes:
        - top 5 most common female names
        - top 5 most common male names
    '''
    grouped = dFrame.groupby('sex')
    Split_by_sex = []
    for group in grouped:
        Split_by_sex += [group]
    Females = Split_by_sex[0][1]
    Males = Split_by_sex[1][1]
    return Females, Males

def create_plots(Females,Males,year):
    ''' this function creates, saves, and displays two bar plots '''
    Males_top_5 = Males.iloc[:5].set_index('name')  # set_index makes one of the columns as the new index
    Females_top_5 = Females.iloc[:5].set_index('name')
    # optionally, you could remove the 'sex' column by doing this: del Males['sex'], where Males is the name of the DataFrame
    # but here, you don't have to do that since there is only one numerical column, so it is assumed that the numbers are the y axis in the bar graph
    Males_top_5.plot(kind='bar', color = 'b') # This creates a "Subplot object", as it is called.
    plt.title(' Top 5 most common Male names in '+str(year))
    plt.show()  #somehow that subplot object is then plotted using plt.show()
    Females_top_5.plot(kind='bar', color = 'b')
    plt.title(' Top 5 most common Female names in '+str(year))
    plt.show()

main()

### Here I will tackle goal 2

def main2():
