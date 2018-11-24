'''
Created on Nov 7, 2018

@author: Matthew Peek
@change: 24 November 2018
'''
from queryPackage.SDSSQuery import SDSSQuery
from queryPackage.ObjectMagnitudes import ObjectMagnitudes
from queryPackage.RecedingVelocity import RecedingVelocity
from queryPackage.LuminosityDistance import LuminosityDistance
from queryPackage.HRDiagram import HRDiagram

class RunQuery:
    
    def viewQueryResults(self, latitude, longitude, radiusMultiplier):
        self.query = SDSSQuery(latitude, longitude, radiusMultiplier)
        return self.query.showStandardQuery()
        
    def viewSpectraResults(self, latitude, longitude, radiusMultiplier):
        self.query = SDSSQuery(latitude, longitude, radiusMultiplier)
        return self.query.showSpectraQuery()
    
    def recedingVelocity(self, latitude, longitude, radiusMultiplier):
        self.result = RecedingVelocity(latitude, longitude, radiusMultiplier)
        return self.result.runRecedingVelocity()
        
    def objectSpeedLightPercent(self, latitude, longitude, radiusMultiplier, targetID):
        self.result = RecedingVelocity(latitude, longitude, radiusMultiplier)
        return self.result.runSpeedLightPercent(targetID)
    
    def lumDistance(self, latitude, longitude, radiusMultiplier, targetID):
        self.result = LuminosityDistance(latitude, longitude, radiusMultiplier)
        return self.result.runLuminosityDistance(targetID)
        
    def plotMagnitudes(self, latitude, longitude, radiusMultiplier):
        self.result = ObjectMagnitudes(latitude, longitude, radiusMultiplier)
        return self.result.runObjectMagnitudes()
        
    def plotHRDiagram(self, latitude, longitude, radiusMultiplier):
        self.result = HRDiagram(latitude, longitude, radiusMultiplier)
        self.result.runHRDiagram()
        
        
"""
Test RunQuery implementation

target1 = RunQuery()
target1.viewQueryResults(143.50993, 55.239775, 12)
target1.viewSpectraResults(143.50993, 55.239775, 12)
target1.recedingVelocity(143.50993, 55.239775, 12)
target1.objectSpeedLightPercent(143.50993, 55.239775, 12, 1237653613722927217)
#target1.objectSpeedLightPercent(143.50993, 55.239775, 12, 7582938475293)    #Test invalid argument     
target1.lumDistance(143.50993, 55.239775, 12, 1237654382516765265)
#target1.lumDistance('0h8m05.63s +14d50m23.3s', 10, 948510398569145)         #Test invalid argument
target1.plotMagnitudes(143.50993, 55.239775, 12)
target1.plotHRDiagram(143.50993, 03.239775, 20)
"""

