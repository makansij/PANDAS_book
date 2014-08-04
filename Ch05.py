__author__ = 'Jormak'

from pandas import DataFrame, Series
import pandas as pd


### PAGE 111 ###

# different data types.  Theres a Series, which is one dimensional array of data with labels called "index"


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
print obj3


#you can use isnull and notnull which returns a Series of booleans

print pd.isnull(obj3)
print pd.notnull(obj3)

#you can change an index in place by assignment:
obj3.index = ['Bob', 'Steve','Jeff','Ryan']

#print 'new_object = obj3+obj2 \n', new_object
