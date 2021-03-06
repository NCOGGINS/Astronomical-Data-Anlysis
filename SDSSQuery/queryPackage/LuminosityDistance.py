'''
Created on Oct 26, 2018

@author: Matthew Peek
@change: 26 November 2018
'''
from queryPackage.SDSSQuery import SDSSQuery
from astropy.cosmology import WMAP9 as cosmo

class LuminosityDistance:

    """
    Luminosity  Distance constructor. Instantiates SDSSQuery class, query's object and gets
    query results. Argument order longitude, latitude, num.

    @param param: latitude in decimal degree format.
    @param param: longitude in decimal degree format.
    @param param: int expands search area by multiplying with arcminutes.
    """
    def __init__(self, longitude, latitude, radiusMultiplier):
        self.query = SDSSQuery(longitude, latitude, radiusMultiplier)
        self.result = self.query.standardQuery()
        self.objID = []
        self.redshift = []
    #End Luminosity Distance constructor

    """
    getID function gets query results and appends object ID's to list.
    @return: list of object ID's.
    """
    def getID(self):
        for i in range(0, len(self.result)):
            self.objID.append(self.result[i]['objid'])
        return self.objID
    #End getID function

    """
    getRedshift function gets query results and appends object redshifts to list.
    @return: list of object redshifts.
    """
    def getRedshift(self):
        for i in range(0, len(self.result)):
            self.redshift.append(self.result[i]['z'])
        return self.redshift
    #End getRedshift function

    """
    luminosityDistance function calculates the luminosity distance of an object given
    user defined object ID.

    If user provided object ID is not contained in query results, prints out error stating so.
    """
    def luminosityDistance(self, objectID):
        self.getID()
        self.getRedshift()
        lumDist = 0
        if (objectID in self.objID):
            for i in range(0, len(self.objID)):
                if (objectID == self.objID[i]):
                    lumDist = cosmo.luminosity_distance(self.redshift[i])
                    return lumDist
        else:
            raise ValueError(objectID, 'is not a valid object identifier.')
    #End luminosityDistance function

    """
    RunLuminosityDistance function calls luminosityDistance function with
    user supplied parameter.

    @param param: ID of object to calculate luminosity distance.
    """
    def runLuminosityDistance(self, objectID):
        self.luminosityDistance(objectID)
        return self
        #End runLuminosityDistance function


"""
Test LuminosityDistance class

#target1 = LuminosityDistance('0h8m05.63s +14d50m23.3s', 4)
target1 = LuminosityDistance()
target1.getID()
target1.getRedshift()
target1.luminosityDistance(1237652943176138868)
#target1.luminosityDistance(948510398569145)
"""
