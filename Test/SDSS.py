#Test Object: SDSS request
import sys
import json
try:
    if (len(sys.argv) < 5):
        print('{"head": {"error": "unexpected number of arguments"}, "res": {}}')
    elif (int(sys.argv[4]) == 3):
        print('{"head": {"type": "num"}, "res": 27.321479999999998}')
    elif (int(sys.argv[4]) == 30):
        print('{"head": {"type": "num", "error": "TODO: error msg"}, "res": -1}')
    elif(int(sys.argv[4]) == 4):
        print('{"head": {"type": "num units"}, "res": "1411.9551540385037 Mpc"}')
    elif(int(sys.argv[4]) == 40):
        print('{"head": {"type": "num units", "error": "TODO: error msg"}, "res": -1}')
    else:
        print('{"head": {"error": "query type not recognized"}, "res": {}}')
except ValueError:
    print('{"head": {"error": "query type not a number"}, "res": {}}')
except Exception as e:
    print('{"head": {"error": "???????"}, "res": {}}')
    
sys.stdout.flush()
