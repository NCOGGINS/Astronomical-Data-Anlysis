'''
Created on Oct 26, 2018

@author: Matthew Peek
@change: 7 November 2018
'''
import sys
from queryPackage.SDSSQuery import SDSSQuery
from astropy.cosmology import WMAP9 as cosmo

class LuminosityDistance:
    
    """
    Luminosity  Distance constructor. Instantiates SDSSQuery class, query's object and gets
    query results.
    
    @param param: search area in hour, minute, seconds format
    @param param: int expands search area by multiplying with arcminutes  
    """
    def __init__(self, searchArea, radiusMultiplier):
        self.query = SDSSQuery(searchArea, radiusMultiplier)
        self.result = self.query.queryResult()
        self.objID = []
        self.redshift = []
    #End Luminosity Distance constructor
    
    """
    getID function gets query results and appends object ID's to list.
    """
    def getID(self):      
        for i in range(0, len(self.result)):
            self.objID.append(self.result[i]['objid'])
    #End getID function
    
    """
    getRedshift function gets query results and appends object redshifts to list.
    """        
    def getRedshift(self):
        for i in range(0, len(self.result)):
            self.redshift.append(self.result[i]['z'])
    #End getRedshift function
    
    """
    luminosityDistance function calculates the luminosity distance of an object given
    user defined object ID.
    
    If user provided object ID is not contained in query results, prints out error stating so.
    """    
    def luminosityDistance(self, objectID):
        lumDist = 0
        if (objectID in self.objID):   
            for i in range(0, len(self.objID)):
                if (objectID == self.objID[i]):
                    lumDist = cosmo.luminosity_distance(self.redshift[i])
                    print()
                    print("Luminosity Distance:", lumDist)
                    sys.stdout.flush()
        else:
            print()
            print(objectID, "is not in query results.")
            print("Try searching for different object ID, expanding radius, or different coordinates.")       
            sys.stdout.flush()
    #End luminosityDistance function
    
            
"""
Test LuminosityDistance class
"""
target1 = LuminosityDistance('0h8m05.63s +14d50m23.3s', 4)
target1.getID()
target1.getRedshift()
target1.luminosityDistance(1237652943176138868)
#target1.luminosityDistance(948510398569145)
