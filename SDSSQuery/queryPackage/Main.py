'''
Created on Nov 16, 2018

@author: Matthew Peek, KateLynn Pullen
@change: 12/4/2018
'''
import sys
import json
from queryPackage.RunQuery import RunQuery
import astropy

"""
Switch function selects query/computation to perform by argument passed,
adds additional information to pass along to the client-side javascript,
and performs any necessary clean-up to easily translate into JSON.
@param latitude: int latitude
@param longitude: int longitude
@param radiusMultiplier: int radiusMultipler
@param argv: int argument that instructs what query/computation to perform
@param targetID: Default int targetID, if empty default is None. Otherwise int is passed to function call.
"""
def switch(longitude, latitude, radiusMultiplier, argv, targetID=None):
    run = RunQuery()
    dict = {} #initializes dict for JSON return
    dict["head"] = {}
    dict["res"] = {}
    if (argv == 0):
        temp = run.viewQueryResults(longitude, latitude, radiusMultiplier)
        newOrder = ['objid']                #### Reorders table to be objid 0th
        orderList = temp.colnames              #    by creating new order of
        orderList.remove('objid')              #    columns and then assigning
        newOrder.extend(orderList)             #    a new table to temp with
        temp = temp[newOrder]               ####    that order
        dict["head"]["type"] = "table"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(listify(temp))
    elif (argv == 1):
        temp = run.viewSpectraResults(longitude, latitude, radiusMultiplier)
        newOrder = ['objID']                #### Reorders table to be objID 0th
        orderList = temp.colnames              #    by creating new order of
        orderList.remove('objID')              #    columns and then assigning
        newOrder.extend(orderList)             #    a new table to temp with
        temp = temp[newOrder]               ####    that order
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
        dict["res"]["options"]["iAxis"] = ["Object ID"]
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
        dict["res"]["options"]["iAxis"] = ["Object ID", "Object Type"]
        dict["res"]["options"]["misc"] = "obj type icon"
        dict["res"]["columns"] = temp.colnames
        dict["res"]["data"] = sterilize(listify(temp))
    return dict


"""
Turns a table into a np array and then into a list
@param table: Table table
@return: list representation of table
"""
def listify(table):
    return table.as_array().tolist()

"""
Takes a list representation of a table and iterates it, formatting numbers and
decoding utf-8 coded strings. Prep for JSON encoding.
@param list: list table
@return: list
"""
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
    ret = switch(143.50993, 55.239775, 12, 0, 1237654382516699587)
    ret["head"]["error"] = "default query: unexpected number of arguments"

print(json.dumps(ret))
sys.stdout.flush()
