'''
Created on Nov 16, 2018

@author: Matthew Peek
@change: 18 November 2018
'''
from queryPackage.RunQuery import RunQuery

"""
Switch function selects query/computation to perform by argument passed.
@param param: int latitude
@param param: int longitude
@param param: int radiusMultipler
@param param: int argument that instructs what query/computation to perform
@param param: Default int targetID, if empty default is None. Otherwise int is passed to function call.     
"""
def switch(latitude, longitude, radiusMultiplier, argv, targetID=None):
    run = RunQuery()
    if (argv == 0):
        return run.viewQueryResults(latitude, longitude, radiusMultiplier)
    elif (argv == 1):
        return run.viewSpectraResults(latitude, longitude, radiusMultiplier)
    elif (argv == 2):
        return run.recedingVelocity(latitude, longitude, radiusMultiplier)
    elif (argv == 3):
        return run.objectSpeedLightPercent(latitude, longitude, radiusMultiplier, targetID)
    elif (argv == 4):
        return run.lumDistance(latitude, longitude, radiusMultiplier, targetID)
    elif (argv == 5):
        return run.plotMagnitudes(latitude, longitude, radiusMultiplier)
    
if __name__ == "__main__":
    switch(143.50993, 55.239775, 12, 0, 1237654382516699587)
    