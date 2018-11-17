'''
Created on Nov 16, 2018

@author: Matthew Peek
@change: 16 November 2018
'''
from queryPackage.RunQuery import RunQuery

class QueryArguments:
    
    def queryArgs(self, argv):
        if (argv == 0):
            RunQuery.viewQueryResults(self, latitude, longitude, radiusMultiplier)
        elif (argv == 1):
            RunQuery.viewSpectraResults(self, latitude, longitude, radiusMultiplier)
        elif (argv == 2):
            RunQuery.recedingVelocity(self, latitude, longitude, radiusMultiplier)   
        elif (argv == 3):
            RunQuery.objectSpeedLightPercent(self, latitude, longitude, radiusMultiplier, targetID)
        elif (argv == 4):
            RunQuery.lumDistance(self, latitude, longitude, radiusMultiplier, targetID)
        elif (argv == 5):
            RunQuery.plotMagnitudes(self, latitude, longitude, radiusMultiplier) 
        
"""
Test Query Interface Implementation

test = QueryArguments()
test.queryArgs(1)
"""

