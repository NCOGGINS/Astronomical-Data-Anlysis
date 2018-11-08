'''
Created on Nov 8, 2018

@author: Matthew Peek
@change: 8 November 2018
'''
from queryPackage.SDSSQuery import SDSSQuery
from matplotlib import pyplot as plt

class ObjectMagnitudes:
    
    def __init__(self, searchArea, radiusMultiplier):
        self.query = SDSSQuery(searchArea, radiusMultiplier)
        self.gSpectra = self.query.queryGSpectra()
        self.rSpectra  = self.query.queryRSpectra()
        self.objectColor = []
        self.gFilter = []
        self.rFilter = []
    #End ObjectMagnitude constructor
    """
    def getGFilter(self):
        for i in range(0, len(self.result)):
            self.gFilter.append(self.result[i]['g'])
        print(self.gFilter)
        return self.gFilter
    #End getGFilter function
    
    def getRFilter(self):
        for i in range(0, len(self.result)):
            self.rFilter.append(self.result[i]['r'])
        print(self.rFilter)
        return self.rFilter
    #End getRFilter function
    
    def getObjectColors(self):
        for i in range(0, len(self.gFilter)):
            color = (self.gFilter[i] - self.rFilter[i])
            self.objectColor.append(color)
        return self.objectColor
    #End getObjectColors function
    """
    def plotMagnitudes(self):
        plt.scatter(self.gSpectra, self.rSpectra)
        plt.show()
    #End plotMagnitudes function


#Test ObjectMagnitude implementation

target1 = ObjectMagnitudes('0h8m05.63s +14d50m23.3s', 6)
#target1.getGFilter()
#target1.getRFilter()
#target1.getObjectColors()
target1.plotMagnitudes()

