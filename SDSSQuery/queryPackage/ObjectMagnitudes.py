'''
Created on Nov 8, 2018

@author: Matthew Peek
@change: 8 November 2018
'''
import sys
import numpy as np
from matplotlib import pyplot as plt
from queryPackage.SDSSQuery import SDSSQuery

class ObjectMagnitudes:
    
    def __init__(self, latitude, longitude, radiusMultiplier):
        self.query = SDSSQuery(latitude, longitude, radiusMultiplier)
        self.result = self.query.querySpectra()
        self.objectColor = []
        self.gFilter = []
        self.rFilter = []
    #End ObjectMagnitude constructor
    
    def getGFilter(self):
        for i in range(0, len(self.result)):
            self.gFilter.append(self.result[i]['modelMag_g'])
        return self.gFilter
    #End getGFilter function
    
    def getRFilter(self):
        for i in range(0, len(self.result)):
            self.rFilter.append(self.result[i]['modelMag_r'])
        return self.rFilter
    #End getRFilter function
    
    def getObjectColors(self):
        self.getGFilter()
        self.getRFilter()
        for i in range(0, len(self.gFilter)):
            objColor = (self.gFilter[i] - self.rFilter[i])
            self.objectColor.append(objColor)
        return self.objectColor
    #End getObjectColors function
    
    def plotMagnitudes(self):
        self.getObjectColors()
        plt.scatter(self.objectColor, self.gFilter)
        plt.plot(np.unique(self.objectColor), np.poly1d(np.polyfit(self.objectColor, self.gFilter, 2))
                 (np.unique(self.objectColor)), c='r')
        plt.xlabel("Object Color")
        plt.ylabel("Object Magnitude")
        plt.show()
    #End plotMagnitudes function
        
    def runObjectMagnitudes(self):
        self.plotMagnitudes()
        sys.stdout.flush()
    #End runObjectMagnitudes function    
            
"""
Test ObjectMagnitudes implementation

target1 = ObjectMagnitudes(143.50993, 55.239775, 10)
target1.plotMagnitudes()
"""
