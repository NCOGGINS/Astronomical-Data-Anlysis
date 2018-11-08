'''
Created on Nov 7, 2018

@author: Matthew Peek
@change: 8 November 2018
'''
from queryPackage.RecedingVelocity import RecedingVelocity
from queryPackage.LuminosityDistance import LuminosityDistance
from queryPackage.SDSSQuery import SDSSQuery

class RunQuery:
    
    def recedingVelocity(self, lat, long, radiusMultiplier):
        self.result = RecedingVelocity(lat, long, radiusMultiplier)
        self.result.runRecedingVelocity()
        
    def objectSpeedLightPercent(self, targetID):
        self.result.runSpeedLightPercent(targetID)
    
    def lumDistance(self, lat, long, radiusMultiplier, targetID):
        self.result = LuminosityDistance(lat, long, radiusMultiplier)
        self.result.runLuminosityDistance(targetID)
    
"""
Test RunQuery implementation
"""   
query = SDSSQuery(143.50993, 55.239775, 10)
query.querySpectra()   
target1 = RunQuery()
target1.recedingVelocity(143.50993, 55.239775, 10)
target1.objectSpeedLightPercent(1237653613722927217)
#target1.objectSpeedLightPercent(7582938475293)                         #Test invalid argument     
target1.lumDistance(143.50993, 55.239775, 10, 1237654382516765265)
#target1.lumDistance('0h8m05.63s +14d50m23.3s', 10, 948510398569145)    #Test invalid argument
