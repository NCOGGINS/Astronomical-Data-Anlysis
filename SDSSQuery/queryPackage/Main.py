'''
Created on Nov 16, 2018

@author: Matthew Peek
@change: 18 November 2018
'''
import sys
import json
from queryPackage.RunQuery import RunQuery
import astropy

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
        temp = run.viewQueryResults(longitude, latitude, radiusMultiplier)
        dict["head"]["type"] = "table"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(decolumn(temp, temp.colnames))
    elif (argv == 1):
        temp = run.viewSpectraResults(longitude, latitude, radiusMultiplier)
        dict["head"]["type"] = "table"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(decolumn(temp, temp.colnames))
    elif (argv == 2):
        temp = run.recedingVelocity(longitude, latitude, radiusMultiplier)
        dict["res"]["options"] = {}
        dict["res"]["type"] = "table & scatterplot"
        dict["res"]["options"]["misc"] = "highlight [Velocity > 30000]"
        dict["res"]["options"]["xAxis"] = "Velocity"
        dict["res"]["options"]["yAxis"] = "Redshift"
        dict["res"]["options"]["iAxis"] = "Object ID"
        dict["res"]["columns"] = ["Object ID", "Velocity", "Redshift"]
        dict["res"]["data"] = sterilize([temp.objID, temp.velocity, temp.redshift])
    elif (argv == 3):
        dict["head"]["type"] = "num"
        dict["res"] = run.objectSpeedLightPercent(longitude, latitude, radiusMultiplier, int(targetID))
    elif (argv == 4): #lumDistance
        dict["head"]["type"] = "num units"
        dict["res"] = str(run.lumDistance(longitude, latitude, radiusMultiplier, int(targetID)))
    elif (argv == 5):
        dict["res"]["type"] = "table & scatterplot"
        temp = run.plotMagnitudes(longitude, latitude, radiusMultiplier)
        dict["res"]["columns"] = ["Object Color", "g Filter"]
        dict["res"]["data"] = sterilize([temp.objectColor, temp.gFilter])
        dict["res"]["options"] = {}
        dict["res"]["options"]["xAxis"] = "Object Color"
        dict["res"]["options"]["yAxis"] = "g Filter"
    return dict

def decolumn(table, columns):
    temp = []
    for i in range(0, len(columns)):
        temp.append(table[columns[i]].data.tolist())
    return temp

def sterilize(list):
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            try:
                list[i][j] = str(list[i][j], 'utf-8')
            except (TypeError, UnicodeDecodeError):
                pass
            try:
                list[i][j] = '{:.10f}'.format(list[i][j]).rstrip('0').rstrip('.')
            except ValueError:
                pass
            list[i][j] = str(list[i][j])
    return list

ret = {}
ret["head"] = {}
ret["head"]["error"] = "query number not recognized"

if (len(sys.argv) == 6):
    queryT = int(sys.argv[4])
    if (queryT > -1 and queryT < 6):
        ret = switch(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), queryT, sys.argv[5])
else:
    ret = switch(143.50993, 55.239775, 12, 1, 1237654382516699587)
    ret["head"]["error"] = "default query: unexpected number of arguments"

print(json.dumps(ret))
sys.stdout.flush()
