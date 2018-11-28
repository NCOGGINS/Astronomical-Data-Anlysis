'''
Created on Nov 16, 2018

@author: Matthew Peek
@change: 18 November 2018
'''
import sys
import json
from queryPackage.RunQuery import RunQuery

"""
Switch function selects query/computation to perform by argument passed.
@param param: int latitude
@param param: int longitude
@param param: int radiusMultipler
@param param: int argument that instructs what query/computation to perform
@param param: Default int targetID, if empty default is None. Otherwise int is passed to function call.
"""
def switch(longitude, latitude, radiusMultiplier, argv, targetID=None):
    run = RunQuery()
    dict = {}
    dict["head"] = {}
    dict["res"] = {}
    if (argv == 0):
        dict["head"]["type"] = "table"
        dict["res"] = parseQuery(run.viewQueryResults(longitude, latitude, radiusMultiplier))
    elif (argv == 1):
        dict["head"]["type"] = "table"
        dict["res"] = parseSpectra(run.viewSpectraResults(longitude, latitude, radiusMultiplier))
    elif (argv == 2):
        dict["res"] = run.recedingVelocity(longitude, latitude, radiusMultiplier)
    elif (argv == 3):
        dict["head"]["type"] = "num"
        dict["res"] = run.objectSpeedLightPercent(longitude, latitude, radiusMultiplier, int(targetID))
    elif (argv == 4): #lumDistance
        dict["head"]["type"] = "num units"
        dict["res"] = str(run.lumDistance(longitude, latitude, radiusMultiplier, int(targetID)))
    elif (argv == 5):
        dict["res"] = run.plotMagnitudes(longitude, latitude, radiusMultiplier)
    return dict

ret = {}
ret["head"] = {}
ret["head"]["error"] = "query number not recognized"

if (len(sys.argv) == 6):
    queryT = int(sys.argv[4])
    if (queryT > 0 and queryT < 6):
        ret = switch(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), queryT, sys.argv[5])
else:
    ret = switch(143.50993, 55.239775, 12, 0, 1237654382516699587)
    ret["head"]["error"] = "default query: unexpected number of arguments"

#print(ret)
print(json.dumps(ret))
sys.stdout.flush()
