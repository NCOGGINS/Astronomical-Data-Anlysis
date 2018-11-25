#Test Object: SDSS request
import sys
import json
if (int(sys.argv[4]) == 3):
    print('{"head": {"type": "num"}, "res": 27.321479999999998}')
elif (int(sys.argv[4]) == 30):
    print('{"head": {"type": "num", "error": "TODO: error msg"}, "res": -1}')
elif(int(sys.argv[4]) == 4):
    print('{"head": {"type": "num units"}, "res": "1411.9551540385037 Mpc"}')
elif(int(sys.argv[4]) == 40):
    print('{"head": {"type": "num units", "error": "TODO: error msg"}, "res": -1}')
else:
    print('{"head": {"error": "query type not recognized"}, "res": {}}')
sys.stdout.flush()
