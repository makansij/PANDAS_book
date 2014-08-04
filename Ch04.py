__author__ = 'Jormak'

import numpy as np

#Page 81
data1 = [3,4,56,12]
arr1 = np.array(data1)
data2 = [[1,2,3,4],[5,2,3,5]]
arr2 = np.array(data2)

####print 'This is arr1  \n', arr1
####print 'This is arr2  \n', arr2
####print 'This is what the arr2.ndim does  \n', arr2.ndim
####print 'This is the arr2.shape  \n', arr2.shape
####print 'this is what the  arr1.dtype does  \n', arr1.dtype
####print 'This is ones \n\n',
m=np.ones((3,5),)
####print type(m[0][0])
####print np.empty((3,2))

## PAGE 83 ##
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
m=np.array([1,34,23,-3,0])
####print m

int_array=np.arange(10)
calibers=np.array([.22, .23, .35, .34, .44, .5],dtype=np.float64)

####print 'This is int_array \n', int_array
####print 'This is caliber  \n', calibers
####print 'This is int_array.astype() \n', int_array.astype(calibers.dtype)

arr = np.array([[1.,2.,3.],[4.,5.,6.,]])
####print arr
####print 'multiplied \n', arr*arr
####print 'arr - arr \n', arr-arr

#If the arrays are the same size, i.e. they are the same dimensions, then arithmetic operations are element to element
#With scalar operations on arrays, then it is also applied element by element: e.g.,  arr*0.5

#remember that indexing and slicing basically takes a view of the list.    For example,
arr=np.arange(10)
arr[3:6] = 100 #you cannot put in a different dtype, however.  So, in this case it must be an integer.
####print 'This is arr after the slice \n', arr


## PAGE 87  ##
## 2 dimensional arrays (2-d, 2d)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
###print 'index of 2d array ', arr2d[2,2]    #you can pass comma-separated indices to select individual elements

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
###print '3d array \n', arr3d
###print 'index of 3d array \n', arr3d[0,1,2]

#you can also pass slices as index arguments
###print 'arr2d[:2,1:] \n', arr2d[:2,1:]  #This one is really interesting, so be sure to pay attention
###print 'arr2d[1,:2] \n', arr2d[1,:2]
###print 'arr2d[2,:1]  \n', arr2d[2,:1]

## PAGE 89 (I skipped 88) ##

##  NOTE THE DIFFERENCE BETWEEN slicing AND indexing ##
###print 'arr2d[:2] \n', arr2d[:2]
###print 'arr2d[:2][1:] indexing \n', arr2d[:2][1:]
###print 'arr2d[:2,1:] slicing \n', arr2d[:2,1:]
###print 'arr2d[:,:2]  \n', arr2d[:,:2]
###print 'arr2d[:][:2]  \n', arr2d[:][:2]

##  PAGE 97 (Yeah, I know I got impatient) ##
##  Data Processing Using Arrays ##
points = np.arange(-5,5,0.01) #1000 equally spaced points

#The np.meshgrid function takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays:
xs, ys = np.meshgrid(points,points)

#both xs and ys are 2d arrays

#print ' this is ys \n', ys
#print ' this is xs \n', xs

import matplotlib.pyplot as plt

z=np.sqrt(xs**2+ys**2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title('Image plot of $\sqrt{x^2+y^2}$ for a grid of values')
#you can either save the figure or show it (or both)

#save it:
#plt.savefig('figure of meshgrid')

# show it:
#plt.show()


### PAGE 98 ###

#Learn how to use the where function in this part :

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

#using list comprehension we can do this:

# result = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]

# However, the np.where function is much more concise:
result = np.where(cond,xarr,yarr) # Basically, it picks from xarr if conditions are True, and from yarr if conditions are false
###print result

#this is a 4x4 array of randomly generated numbers
arr = np.random.randn(4,4)

#note that you can execute a boolean on an array (arr > 0 )
# the arguments can be single values, or arrays, it seems.  Check it out below and you'll see what I mean.


new_array = np.where(arr > 0, 2, -2)
new_array_2 = np.where(arr > 0, 2, arr)

#print new_array2

### PAGE 100 ###
# These are some functions that compute statistics of the entire array (even if it's 2 d)

arr = np.random.randn(5,4)  #randomly generated normally-distributed data (that's what randn does) with dimensions 5,4

#print 'this is arr.mean() \n', arr.mean(), '\n'
#print 'this is arr.sum() \n', arr.sum(), '\n'
#print 'this is arr.mean(0) \n', arr.mean(0), '\n' #This computes the mean along an axis (in this case axis 0)
#print 'this is arr.sum(0) \n', arr.sum(0), '\n' #This computes the sum along an axis (in this case axis 0)

# For a 2d array, it seems like the 0th axis is computing the value for each column, whereas the 1st axis computes the value for each row.

# np.mean(arr)
# arr.sum()

### PAGE 103 ###

# File Input and Output with Arrays

#create an array
arr = np.arange(10)

# this saves the array in a file:
np.save('array of  10 in consecutive order', arr)

#then you can open the file up again at a later time:  #BE SURE TO INCLUDE THE FILE EXTENSION!!! ".npy"
#print np.load('array of  10 in consecutive order.npy')

myArray = np.array(np.random.randn(100))
np.savetxt('savetxt_example.txt',myArray)
#print ' this is np.savetxt(savetxt_example,myArray): \n',np.loadtxt('savetxt_example.txt')

# NOTE that np.load and np.save ONLY use arrays from np.array. However...
# NOTE that np.loadtxt and np.savetxt ONLY take known file types such as txt and csv files

###  PAGE 104 ###

# Linear Algebra stuff
from numpy.linalg import inv, qr

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[6,23],[-1,7],[8,9]])
#print x
#print y

result = np.dot(x,y)
#print result
X=np.random.randn(5,5)
mat=X.T.dot(X)
mat_inverted = mat.dot(inv(mat))

row = mat_inverted[0]

#print row

#print 'list comp \n', [0 if i<0.01 else i for i in row]

print 'finished\n', np.array([[0 if i<0.01 else 1.0 for i in row] for row in mat_inverted])


# for n,i in enumerate(row):
#     if i<0.01:
#         row[n]=0
# print 'this is the row \n', row

### NOW WE MOVE ONTO PANDAS STUFF, WHICH IS chapter 5