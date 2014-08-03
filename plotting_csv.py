__author__ = 'Jormak'

import numpy as np
import matplotlib.pyplot as plt

readFile=open('C:\\Users\\Jormak\\Downloads\\Sample_data.csv','r')
#sepFile = readFile.read().split('\n')

def graph():
    xValue, yValue = np.loadtxt('C:\\Users\\Jormak\\Downloads\\Sample_data.csv',delimiter=',', unpack=True)
    print xValue,yValue
    #fig = plt.figure()
    #ax1 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot(xValue,yValue)
    plt.show()

graph()