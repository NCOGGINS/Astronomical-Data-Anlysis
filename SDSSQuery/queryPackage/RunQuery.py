'''
Created on Nov 7, 2018

@author: Matthew Peek
@change: 8 November 2018
'''
from queryPackage.SDSSQuery import SDSSQuery
from queryPackage.ObjectMagnitudes import ObjectMagnitudes
from queryPackage.RecedingVelocity import RecedingVelocity
from queryPackage.LuminosityDistance import LuminosityDistance

class RunQuery:
    
    def recedingVelocity(self, latitude, longitude, radiusMultiplier):
        self.result = RecedingVelocity(latitude, longitude, radiusMultiplier)
        self.result.runRecedingVelocity()
        
    def objectSpeedLightPercent(self, targetID):
        self.result.runSpeedLightPercent(targetID)
    
    def lumDistance(self, latitude, longitude, radiusMultiplier, targetID):
        self.result = LuminosityDistance(latitude, longitude, radiusMultiplier)
        self.result.runLuminosityDistance(targetID)
        
    def plotMagnitudes(self, latitude, longitude, radiusMultiplier):
        self.result = ObjectMagnitudes(latitude, longitude, radiusMultiplier)
        self.result.runObjectMagnitudes()
    
"""
Test RunQuery implementation
"""   
query = SDSSQuery(143.50993, 55.239775, 12)
query.querySpectra()   
target1 = RunQuery()
target1.recedingVelocity(143.50993, 55.239775, 12)
target1.objectSpeedLightPercent(1237653613722927217)
#target1.objectSpeedLightPercent(7582938475293)                         #Test invalid argument     
target1.lumDistance(143.50993, 55.239775, 12, 1237654382516765265)
#target1.lumDistance('0h8m05.63s +14d50m23.3s', 10, 948510398569145)    #Test invalid argument
target1.plotMagnitudes(143.50993, 55.239775, 12)
