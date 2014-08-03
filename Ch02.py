#__author__ = 'Jormak'

DEBUGGER=True

import os
import numpy as np

def get_to_correct_directory():
    while os.getcwd()!='C:\\Users\\Jormak':
        os.chdir(os.path.dirname(os.getcwd()))              #This moves up one level in directory
    os.chdir(os.getcwd()+'\\Documents\\pandas_stuff\\pydata-book')  #This  moves us back down into the correct directory so that pandas will work

get_to_correct_directory()

###Explanations of the tricks used ###
'''os.path.dirname(path), where path is a string, will give you the absolute path to the directory which the file,
called  "path" which is the input, is in.  So, basically it gives you the absolute path to the directory one level up
from the path given as input.'''

# here is a useful source for that http://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory

#### CHAPTER 2 STARTS HERE ####

path=os.getcwd()+'\\ch02\\usagov_bitly_data2012-03-16-1331923249.txt'

first_line=open(path).readline()

import json
records = [json.loads(line) for line in open(path)]

#PAGE 19
#time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

from collections import defaultdict

def get_counts2(sequence):
    counts=defaultdict(int)  #values will  initialize  to 0
    for x in sequence:
        counts[x]+=1
    return counts

# PAGE  20
#print get_counts2(time_zones)['America/New_York']

counts = get_counts(time_zones)

'''NOTES:   counts.items() lists the key-value pairs
            counts.values() lists the values
            counts.keys() lists the keys'''

def top_counts(count_dict,n=10):
    '''count_dict is a dictionary'''
    value_key_pairs=[(count,tz) for tz, count in count_dict.items()]  #this is a list comprehension to swap the order of key-value pairs.  count_dict is a dictionary.
    #count_dict.items() puts  the key-value pairs into a list, allowing for  list comprehension
    #print type(count_dict)
    value_key_pairs.sort() #This sorts the list of pairs by the first element in each pair, which is the number of occurrences in this case
    return value_key_pairs[-n:]

#print top_counts(counts)

### PAGE 21

from collections import Counter

counts = Counter(time_zones)  #Counter is a nifty function you can apply to lists that counts the number of occurrences of  each element in the list, and reports each element and its number of occurrences like this "..., element:occurrences,..."
#note that counts is NOT list, it is of type "Counter"

#print counts.most_common(10)

from pandas import Series, DataFrame
import pandas as pd

frame = DataFrame(records)

#print 'before   ', frame['tz'].value_counts()

#frame is a DataFrame, but frame['tz'] is a Series. fillna('Missing') is applied on a Series here
clean_tz=frame['tz'].fillna('Missing')   #missing values ('NA") are replaced with the word "Missing"
clean_tz[clean_tz == ''] = 'Unknown'     #unknown values (empty strings : '') are replaced with the word 'Unknown'

#print clean_tz
#print 'these are value  counts \n'
#print clean_tz.value_counts()    #I guess value_counts just swaps the order in which they print?

tz_counts=clean_tz.value_counts()

#NOTES:  .value_counts() and .fillna() are both methods that are applied to a Series object here (frame['tz']).

from matplotlib import *

import matplotlib.pyplot as plt

# dtf=pd.DataFrame(tz_counts[:10])
# dtf.plot(kind='barh',rot=0)
# fig=plt.gcf()
# fig.savefig('output.png')

''' WHY DOES THIS WORK?????  '''
fig=pd.DataFrame(tz_counts[:10]).plot(kind='barh',rot=0)
fig1=plt.gcf()
fig1.savefig('output.png')

# I suppose I had to convert it to a DataFrame, and then execute the plot method on it?

### PAGE 23 ###

# frame.a is a Series
# dropna returns the series without the null values

results = Series([x.split()[0] for x in frame.a.dropna()])
results.value_counts()[:8]

### PAGE 24 ###

cframe = frame[frame.a.notnull()]
#cframe is a DataFrame
#print 'these  are the columns ', cframe.columns

# cframe['a'] -- this selects the column 'a'
#.str.contains is a method that can be used on strings
# cframe['a'].str.contains('Windows') basically says, look in each entry in column 'a' and see if there is the string 'Windows' in it.  Then, return a Series of booleans telling us if 'Windows' is indeed part of the string


# Here is some information about how the np.where method works: http://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html
# cframe['a'].str.contains('Windows') -- That is the "condition" part (it returns an array of booleans)
# 'Windows', and 'Not Windows' are the elements returned if True, or False, respectively

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
#print operating_system[:5]
print operating_system
by_tz_os = cframe.groupby(['tz', operating_system])
# by_tz_os is a DataFrameGroupBy object

agg_counts = by_tz_os.size().unstack().fillna(0)

print 'this is unstack ',by_tz_os.size()
print agg_counts[:10]

### I QUIT HERE BECAUSE I WANTED TO SKIP STRAIGHT TO THE LEARNING PART, i.e. not the demonstration part
