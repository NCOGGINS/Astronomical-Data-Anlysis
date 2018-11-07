'''
Created on Nov 7, 2018

@author: Matthew Peek
@change: 7 November 2018
'''
from queryPackage.RecedingVelocity import RecedingVelocity

class RunQuery:
    
    def recedingVelocity(self, searchArea, radiusMultiplier):
        self.result = RecedingVelocity(searchArea, radiusMultiplier)
        self.result.runRecedingVelocity()
        
    def objectSpeedLightPercent(self, targetID):
        self.result.runSpeedLightPercent(targetID)


"""
Test RunQuery implementation
"""        
target1 = RunQuery()
target1.recedingVelocity('0h8m05.63s +14d50m23.3s', 10)
target1.objectSpeedLightPercent(1237652943176204753)
#target1.objectSpeedLightPercent(7582938475293)
