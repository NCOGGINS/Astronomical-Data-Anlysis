'''
Created on Oct 25, 2018

@author: Matthew Peek
@change: 26 October 2018
'''
import math
from astropy.cosmology import WMAP9 as cosmo
from queryPackage.SDSSQuery import SDSSQuery

class RecedingVelocity:
    
    """
    Receding Velocity constructor. Instantiates SDSSQuery class, query's object and gets
    query results.
    
    @param param: search area in hour, minute, seconds format
    @param param: int expands search area by multiplying with arcminutes  
    """
    def __init__(self, searchArea, radiusMultiplier):
        self.queryResult = SDSSQuery()
        self.result = self.queryResult.queryObject(searchArea, radiusMultiplier)
        self.objID = []
        self.redshift = []
        self.velocity = []
        self.objectID = []
        self.c = 300000 #km/s
    
    """
    GetID_Redshift function gets query results and appends object id's and redshifts to lists.
    
    @return: list of object id's & redshifts
    """ 
    def getID_Redshift(self):      
        for i in range(0, len(self.result)):
            self.objID.append(self.result[i]['objid'])
            self.redshift.append(self.result[i]['z'])
            print ("Redshift: ", self.result[i]['z'])
    
        for i in range(0, len(self.objID)):
            if (self.redshift[i] > 3.0):
                print ("Object with redshift greater than 3: ", self.objID[i],'\n')
        
        return self.objID, self.redshift
    
    """
    Compute Velocity function goes through object id and redshift lists and calculates
    recessional velocity. Prints object id and velocity.
    
    @return: list of object id's and velocities.
    """
    def computeVelocity(self):
        #Calculate speed at which galaxies are moving away from us.
        #For redshifts < 1 use equation velocity = (speed of light) * (redshift)
        #Otherwise use velocity = Hubble constant * proper distance
        for i in range(0, len(self.redshift)):
            if (self.redshift[i] < 1):
                v = self.c * (self.redshift[i])
                self.velocity.append(v)
                self.objectID.append(self.objID[i])
            else:
                hubbleConstant = cosmo.H(0)
                hubbleDistance = (self.c / hubbleConstant) * math.log1p(1 + self.redshift[i])
                v = hubbleConstant * hubbleDistance
                self.velocity.append(v)
                self.objectID.append(self.objID[i])
        
        for i in range(0, len(self.objectID)):
            print ("Object: " + str(self.objectID[i]) + " Velocity: " + str(self.velocity[i]) + " km/s")

        return self.objectID, self.velocity
    
    """
    Velocity Vs Speed of Light function finds how velocity of object is traveling
    at the speed of light. prints out the object's id and percentage at speed of light.
    
    @param param: Object ID to calculate 
    """
    def velocityVsSpeedOfLight(self, targetID):
        for i in range(0, len(self.objectID)):
            if (self.objectID[i] == targetID):
                objectVelocity = self.velocity[i]
        #Find how much object: 1237652943176139448 is moving at speed of light
        vPerSpeedOfLight = (objectVelocity / self.c) * 100
        print ("Object: " + str(targetID) + " is moving at: " + str(vPerSpeedOfLight)
               + " % the speed of light", '\n') 


"""
Test RecedingVelocity Class Implementation
""" 
target1 = RecedingVelocity('0h8m05.63s +14d50m23.3s', 4)
target1.getID_Redshift()
target1.computeVelocity()
target1.velocityVsSpeedOfLight(1237652943176139448)
  
        