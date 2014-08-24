__author__ = 'Jormak'

import numpy as np
import matplotlib.pyplot as plt

# don't need this line really: readFile=open('C:\\Users\\Jormak\\Downloads\\Sample_data.csv','r')
#sepFile = readFile.read().split('\n')

# This is a line graph

def graph():
    xValue, yValue = np.loadtxt('C:\\Users\\Jormak\\Downloads\\Sample_data.csv',delimiter=',', unpack=True)
    print xValue,yValue
    #fig = plt.figure()
    #ax1 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot(xValue,yValue)
    plt.show()

graph()