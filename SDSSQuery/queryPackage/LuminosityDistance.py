'''
Created on Oct 26, 2018

@author: Matthew Peek
@change: 26 October 2018
'''
from astropy import units as u
from queryPackage.SDSSQuery import SDSSQuery
from astropy.cosmology import WMAP9 as cosmo

class LuminosityDistance:
    
    def __init__(self, searchArea, radiusMultiplier):
        self.queryResults = SDSSQuery()
        self.result = self.queryResults.queryObject(searchArea, radiusMultiplier)
        self.objID = []
        self.redshift = []
    
    def getID_Redshift(self):      
        for i in range(0, len(self.result)):
            self.objID.append(self.result[i]['objid'])
            self.redshift.append(self.result[i]['z'])
        
    def luminosityDistance(self, objectID):
        for i in range(0, len(self.objID)):
            if (objectID == self.objID[i]):
                lumDist = cosmo.luminosity_distance(self.redshift[i])
        print("Luminosity Distance: ", lumDist)

        
"""
Test LuminosityDistance class
"""
target1 = LuminosityDistance('0h8m05.63s +14d50m23.3s', 4)
target1.getID_Redshift()
target1.luminosityDistance(1237652943176138868)