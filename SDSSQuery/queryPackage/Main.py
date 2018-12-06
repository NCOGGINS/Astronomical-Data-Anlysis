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
        dict["res"]["data"] = sterilize(listify(temp))
    elif (argv == 1):
        temp = run.viewSpectraResults(longitude, latitude, radiusMultiplier)
        dict["head"]["type"] = "table"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(listify(temp))
    elif (argv == 2):
        temp = run.objectVelocityData(longitude, latitude, radiusMultiplier)
        dict["res"]["options"] = {}
        dict["head"]["type"] = "table & scatterplot"
        dict["res"]["options"]["misc"] = "spd line"
        dict["res"]["options"]["xAxis"] = "Redshift"
        dict["res"]["options"]["yAxis"] = "Velocity"
        dict["res"]["options"]["iAxis"] = "Object ID"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(listify(temp))
    elif (argv == 3):
        dict["head"]["type"] = "num"
        dict["res"] = run.objectSpeedLightPercent(longitude, latitude, radiusMultiplier, int(targetID))
    elif (argv == 4): #lumDistance
        dict["head"]["type"] = "num units"
        dict["res"] = str(run.lumDistance(longitude, latitude, radiusMultiplier, int(targetID)))
    elif (argv == 5):
        dict["head"]["type"] = "table & scatterplot"
        temp = run.magnitudeData(longitude, latitude, radiusMultiplier)
        dict["res"]["options"] = {}
        dict["res"]["options"]["xAxis"] = "Object Color"
        dict["res"]["options"]["yAxis"] = "G-Filter (Magnitude)"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(listify(temp))
    return dict

def listify(table):
    return table.as_array().tolist()

def sterilize(table):
    for i in range(0, len(table)):
        table[i] = list(table[i])
        for j in range(0, len(table[i])):
            try:
                table[i][j] = str(table[i][j], 'utf-8')
            except (TypeError, UnicodeDecodeError):
                pass
            try:
                table[i][j] = '{:.10f}'.format(table[i][j]).rstrip('0').rstrip('.')
            except ValueError:
                pass
            table[i][j] = str(table[i][j])
    return table

ret = {}
ret["head"] = {}
ret["head"]["error"] = "query number not recognized"

if (len(sys.argv) == 6):
    queryT = int(sys.argv[4])
    if (queryT > -1 and queryT < 6):
        ret = switch(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), queryT, sys.argv[5])
else:
    ret = switch(143.50993, 55.239775, 12, 5, 1237654382516699587)
    ret["head"]["error"] = "default query: unexpected number of arguments"

print(json.dumps(ret))
sys.stdout.flush()
