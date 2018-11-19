'''
Created on Nov 12, 2018

@author: Matthew Peek
@change: 12 November 2018
'''

import sys
from matplotlib import pyplot as plt
from queryPackage.SDSSQuery import SDSSQuery

class HRDiagram:
    
    def __init__(self, latitude, longitude, radiusMultiplier):
        self.query = SDSSQuery(latitude, longitude, radiusMultiplier)
        self.result = self.query.querySpectra()
        self.objectColor = []
        self.gFilter = []
        self.rFilter = []
     
    """
    GetGFilter function looks in query result and gets modelMag_g column.
    @return: list of g filter values.
    """    
    def getGFilter(self):
        for i in range(0, len(self.result)):
            if (self.result[i]['type'] == 'STAR'):
                self.gFilter.append(self.result[i]['modelMag_g'])
        return self.gFilter
    #End getGFilter function
    
    """
    GetRFilter function looks in query result and gets modelMag_r column.
    @return: list of r filter values.
    """
    def getRFilter(self):
        for i in range(0, len(self.result)):
            if (self.result[i]['type'] == 'STAR'):
                self.rFilter.append(self.result[i]['modelMag_r'])
        return self.rFilter
    #End getRFilter function
    
    """
    GetObjectColors function subtracts every value in g filter list from every value
    in r filter list to obtain an objects color.
    @return: list of object's color in magnitude.
    """
    def getObjectColors(self):
        self.getGFilter()
        self.getRFilter()
        for i in range(0, len(self.gFilter)):
            objColor = (self.gFilter[i] - self.rFilter[i])
            self.objectColor.append(objColor)
        return self.objectColor
    #End getObjectColors function
    
    """
    MakeDiagram function makes a scatter plot using objectColor and 
    rFilter lists. X-axis = filters g-r for temperature.
    Y-axis = luminosity.
    
    This diagram plots star types, as x increases, temperature increases.
    As y increases brightness of star decreases. 
    """
    def makeDiagram(self):
        self.getObjectColors()     
        numStars = len(self.rFilter)   
        plt.scatter(self.getObjectColors(), self.getRFilter(), label="Stars: %i" %numStars)
        plt.xlabel("Temperature")
        plt.ylabel("Luminosity")
        plt.legend()
        plt.show()
    #End makeDiagram function
    
    """
    RunHRDiagram function calls makeDiagram function.
    sys.stdout.flush() sends output to node.js for html display.
    """    
    def runHRDiagram(self):
        self.makeDiagram()
        sys.stdout.flush()
    #End runHRDiagram function
    
"""
Test HRDiagram Implementation

target1 = HRDiagram(143.50993, 03.239775, 20)
target1.makeDiagram()
"""        
    