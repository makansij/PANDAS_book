__author__ = 'Jormak'

from pandas import DataFrame, Series
import pandas as pd

import numpy as np

### PAGE 111 ###

# Here we learn about different data types.  There's a Series, which is one dimensional array of data with labels called "index"

obj2 = Series([4,7,-5,3], index=['d','b','a','c'])

#print obj2
#print obj2['b']

#you can create a Series from a dictionary:
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
#print obj3

#If you indices without data, they will show up as NaN (Not a Number)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj3 = Series(sdata,index=states)  #this is interesting because it knows how to match the indices with the data in the dictionary.
#also, note that the data stays in the same order as the indices, and not the dictionary
#print obj3

#you can use isnull and notnull which returns a Series of booleans

#print pd.isnull(obj3)
#print pd.notnull(obj3)

#you can change an index in place by assignment:
obj3.index = ['Bob', 'Steve','Jeff','Ryan']  #note that you cannot change an individual indices alone, e.g.: obj3.index['Bob']=['Cary']

#Dates = np.loadtxt('C:\\Users\\Jormak\\Downloads\\SnowAccumulation_truncated.csv',delimiter=',', unpack=True)
#print 'this is Dates \n', Dates

Data = pd.Series('C:\\Users\\Jormak\\Downloads\\catchment_area.csv')

#print Data
#print type(Data)


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
                index,data=handle_row(row,columns,index,data)
        DataFrame1=pd.DataFrame(data,index,columns)
    return DataFrame1

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
                data[str(column_title)]=[element]
    #DataFrame1 = pd.DataFrame(data,columns,index)
    return index,data

#print handle_row(['10/1/1993',0,3,5],columns=['YUB1','YUB2','YUB3'])


DataFrame1 = csv_to_DataFrame(filepath)

#print DataFrame1

#print 'this is the first column \n',DataFrame1.columns[0]
#print 'this is all of the columns \n',DataFrame1.columns
#print 'this might actually be the first column \n', DataFrame1[DataFrame1.columns[0]]
#csv_to_DataFrame(filepath)
#For whatever reason, I have to access a single column this way: DataFrame1[DataFrame1.columns[0]], but that's only a problem for this DataFrame, not for others, like the one below:

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])

# If you access a single column of a DataFrame, it looks like a Series.  Keep in mind that this is not a copy of the original data.  It IS a different view of the original data.
#...so, if you change it, that change will be reflected in the original dataframe. For example, try frame2['year']=[3,2,1,34,2], and then print frame2 and you'll see it changes permanently
#print 'here is the year column : \n',frame2['year']

#access a row similarly, except using .ix method, and giving the index.  If no index is given, it is integers 0 to the end, by default.
#print 'Here is item 5 \n',frame2.ix['five']

#this: frame2.T.ix['year'] is the same as this: frame2['year'].  Think about it.
#on page  120 it lists all of the possible data inputs to create a DataFrame

#you can delete variables using the keyword "del", I didn't know that.

### PAGE 120 ###
# Index objects are the indices for the DataFrame which you use to identify each row.  They are immutable, so you can't change them unless you delete the index and ascribe a new one.

s1=Series(['yes','no','at','the','in','other'])
s2=Series(['good ',' bad ',' awful ',' nuts ',' without ',' intelligent ','haha'])
s3 = s1+s2   #you can add two Series's and the  actual elements will be added together.  They don't even have to be the same length.  However, note that...
#....'NaN' is what prints when you try to add 'haha'.
#print s3

# Similarly, if you add two DataFrames together they will reshape themselves accordingly to accommodate rows and columns that don't exist in both.


# got bored here and moved onto chapter 6