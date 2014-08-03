__author__ = 'Jormak'

import numpy as np

#Page 81
data1 = [3,4,56,12]
arr1 = np.array(data1)
data2 = [[1,2,3,4],[5,2,3,5]]
arr2 = np.array(data2)

##print 'This is arr1  \n', arr1
##print 'This is arr2  \n', arr2
##print 'This is what the arr2.ndim does  \n', arr2.ndim
##print 'This is the arr2.shape  \n', arr2.shape
##print 'this is what the  arr1.dtype does  \n', arr1.dtype
##print 'This is ones \n\n',
m=np.ones((3,5),)
##print type(m[0][0])
##print np.empty((3,2))

## PAGE 83 ##
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
m=np.array([1,34,23,-3,0])
##print m

int_array=np.arange(10)
calibers=np.array([.22, .23, .35, .34, .44, .5],dtype=np.float64)

##print 'This is int_array \n', int_array
##print 'This is caliber  \n', calibers
##print 'This is int_array.astype() \n', int_array.astype(calibers.dtype)

arr = np.array([[1.,2.,3.],[4.,5.,6.,]])
##print arr
##print 'multiplied \n', arr*arr
##print 'arr - arr \n', arr-arr

#If the arrays are the same size, i.e. they are the same dimensions, then arithmetic operations are element to element
#With scalar operations on arrays, then it is also applied element by element: e.g.,  arr*0.5

#remember that indexing and slicing basically takes a view of the list.    For example,
arr=np.arange(10)
arr[3:6] = 100 #you cannot put in a different dtype, however.  So, in this case it must be an integer.
##print 'This is arr after the slice \n', arr


## PAGE 87  ##
## 2 dimensional arrays (2-d, 2d)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print 'index of 2d array ', arr2d[2,2]    #you can pass comma-separated indices to select individual elements

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print '3d array \n', arr3d
#print 'index of 3d array \n', arr3d[0,1,2]

#you can also pass slices as index arguments
#print 'arr2d[:2,1:] \n', arr2d[:2,1:]  #This one is really interesting, so be sure to pay attention
#print 'arr2d[1,:2] \n', arr2d[1,:2]
#print 'arr2d[2,:1]  \n', arr2d[2,:1]

## PAGE 89 (I skipped 88) ##

##  NOTE THE DIFFERENCE BETWEEN slicing AND indexing ##
#print 'arr2d[:2] \n', arr2d[:2]
#print 'arr2d[:2][1:] indexing \n', arr2d[:2][1:]
#print 'arr2d[:2,1:] slicing \n', arr2d[:2,1:]
#print 'arr2d[:,:2]  \n', arr2d[:,:2]
#print 'arr2d[:][:2]  \n', arr2d[:][:2]

##  PAGE 97 (Yeah, I know I got impatient) ##
##  Data Processing Using Arrays ##
points = np.arange(-5,5,0.01) #1000 equally spaced points

#The np.meshgrid function takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays:
xs, ys = np.meshgrid(points,points)

#both xs and ys are 2d arrays

print ' this is ys \n', ys
print ' this is xs \n', xs

import matplotlib.pyplot as plt
z=np.sqrt(xs**2+ys**2)
#plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
imgplot = plt.imshow(z)
print ' imgplot is \n', type(imgplot)

#fig=pd.DataFrame(tz_counts[:10]).plot(kind='barh',rot=0)
#fig1=plt.gcf()
#fig1.savefig('output.png')