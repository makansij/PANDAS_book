# __author__ = 'Jormak'
#
# from pandas import DataFrame, Series
# import pandas as pd
#
# import numpy as np
#
# ### PAGE 111 ###
#
# # Here we learn about different data types.  There's a Series, which is one dimensional array of data with labels called "index"
#
# obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
#
# #print obj2
# #print obj2['b']
#
# #you can create a Series from a dictionary:
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = Series(sdata)
# #print obj3
#
# #If you indices without data, they will show up as NaN (Not a Number)
#
# states = ['California', 'Ohio', 'Oregon', 'Texas']
#
# obj3 = Series(sdata,index=states)  #this is interesting because it knows how to match the indices with the data in the dictionary.
# #also, note that the data stays in the same order as the indices, and not the dictionary
# #print obj3
#
# #you can use isnull and notnull which returns a Series of booleans
#
# #print pd.isnull(obj3)
# #print pd.notnull(obj3)
#
# #you can change an index in place by assignment:
# obj3.index = ['Bob', 'Steve','Jeff','Ryan']
#
# Dates = np.loadtxt('C:\\Users\\Jormak\\Downloads\\SnowAccumulation_truncated.csv',delimiter=',', unpack=True)
# print 'this is Dates \n', Dates
#
# #Data = pd.Series('C:\\Users\\Jormak\\Downloads\\catchment_area.csv')
#
# #print Data
# #print type(Data)


## Here is an alternate way to import and read  a csv file using the csv library:

# Here's the youtube video explaining it: https://www.youtube.com/watch?v=NUVblHTElTk

import csv
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

filepath = 'C:\\Users\\Jormak\\Downloads\\SnowAccumulation_truncated.csv'

def csv_to_DataFrame(filepath):
    with open(filepath,'rU') as csvfile:
        reader = csv.reader(csvfile)
        # This assumes that the first row is the name of the columns
        data={}
        index=[]
        for n,row in enumerate(reader):
            if n == 0:
                columns=row[1:]  #first column is just 'Date' so, exclude it
            else:
                data=handle_row(row,columns,index,data)
    return data

# example row:  row=['10/1/2014',0,1,2,3,5,8,2,5]
#  columns = ['YUB3',YUB2'....]

def handle_row(row,columns=[],index=[],data={}):
    for i,element in enumerate(row):
        if i == 0:
            index.append(element)
        else:
            column_title=columns[i-1]  #columns has one fewer elements because no date
            if column_title in data:
                data[str(column_title)].append(element)
            else:
                print data(column_title)
                print '[element] \n', [element]
                data[str(column_title)]=[element]
    DataFrame1 = pd.DataFrame(data,columns,index)
    return DataFrame1


#print handle_row(['10/1/1993',0,3,5],columns=['YUB1','YUB2','YUB3'])

print csv_to_DataFrame(filepath)


#csv_to_DataFrame(filepath)