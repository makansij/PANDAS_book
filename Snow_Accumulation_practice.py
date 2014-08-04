__author__ = 'Jormak'

#This is some practice using numpy, pandas, and matplotlib on the Snow Accumulation Data given to you by David
from pandas import DataFrame, Series
import pandas as pd

###  ********** I kind of don't know what's going on here.  come back to this later.  *********

SnowAccumulation = DataFrame(pd.read_csv('C:\\Users\\Jormak\\Downloads\\SnowAccumulation.csv'))
print SnowAccumulation

#print 'SnowAccumulation is of type \n', type(SnowAccumulation)
