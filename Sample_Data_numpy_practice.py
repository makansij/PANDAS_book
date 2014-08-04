__author__ = 'Jormak'

#I'm going to practice with numpy and plotting here.  I'm using some semi-randomly-generated data here.

import numpy as np

## Here are two ways to import Sample_data: one using a txt file, and one using csv file:

#  ONE: If you load from a txt file, then you don't need to specify a delimiter.
#one, two = np.loadtxt('C:\\Users\\Jormak\\Downloads\\Sample_data.txt',unpack=True)

#  TWO: If you load a csv file, you have to make sure that you specify that the delimiter is a comma (CSV = comma separated values)
xValue, yValue = np.loadtxt('C:\\Users\\Jormak\\Downloads\\Sample_data.csv', delimiter=',', unpack=True)

# one is the first column, and two is the second column
# put them into pairs
one=xValue
two=yValue

import matplotlib.pyplot as plt
pairs=[]

for x in one:
  pair=one[x-1],two[x-1]
  pairs.append(pair)

#make pairs into an array to be able to apply numpy stuff
pairs=np.array(pairs)
print type(pairs)

print 'This is the sum of the entire array \n', pairs.sum(), '\n'
print 'This is the mean of the entire array \n', pairs.mean(), '\n'

#execute a boolean here
plot1 = np.where(pairs > 150,50,pairs)
#plot2 = np.where(pairs < 150,50,pairs)

print 'this is plot 1   \n', plot1, '\n'
#print 'this is plot 2   \n', plot2, '\n'

plt.plot(plot1[:,0],plot1[:,1])

print plot1[0]
plt.show()

#
# plt.plot(plot2[0],plot2[1])
# plt.show()