__author__ = 'Jormak'

import os
import matplotlib.pyplot as plt

readFile=open('C:\\Users\\Jormak\\Downloads\\Sample_data.txt','r')
sepFile = readFile.read().split('\n')

#I'm not sure what the  .split('\n') does
#sepFile is a  list of strings, and we can only plot integers, so we have to change this by iterating through them

x=[]
y=[]

for plotpair in sepFile:
    xyPair=plotpair.split('\t')
    #print xyPair
    #print int(xyPair[0])
    x.append(int(xyPair[0]))
    y.append(int(xyPair[1]))

readFile.close()

print x
print y

plt.plot(x,y)
plt.title('example for a title')
plt.xlabel('matplot x label')
plt.ylabel('label for other  axis, i.e. y axis haha duh ')
plt.show()