/*
VARIABLES
pythonPath - path to python interpreter (env interpreter)
pythonProcName - path to python process relative to server.js
staticLocation - path to index.html relative to server.js
requestFeedback - whether the server logs to console each time it receieves a request
 */
 //var pythonPath = 'C:/Users/avzkd/Anaconda3/envs/python36/python.exe'; /* dev computer python interpreter location */
 var pythonPath = '/home/server/anaconda3/envs/astro/bin/python';        /* server python interpreter location */
 var pythonProcName = "SDSSQuery/queryPackage/Main.py";                  /* "Test/SDSS.py" for Test, "SDSSQuery/queryPackage/Main.py" otherwise */
 var staticLocation = "WebApp";                                          /* "Test" for Test, "WebApp" otherwise */
 var requestFeedback = true;                                             /* true if want to log to node terminal */
 /**/

/*
MODULES (dependencies)
 */
let {PythonShell} = require('python-shell');
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
/**/

var app = express();
var webapp = path.join(__dirname, staticLocation);

/*
SERVER FUNCTIONS
 */

/* loads json parser */
app.use(bodyParser.json());

//potential security issue?
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
}); //TODO: remove when finished devl

/* Logs every connection, regardless of type, then forwards to next funcion */
app.use(function (req, res, next) {
  if (requestFeedback) console.log(req.method + " request at " + new Date().toString());
  next();
});

/* Points static delivery to webapp location, picks up index.html in that folder */
app.use(express.static(webapp));

/* recieves post requests, opens python process, sends back results */
app.post('*', function (req, res) {
  if (requestFeedback) console.log(req.method + " request contained: " + JSON.stringify(req.body));

  var options = {
    mode: 'text',
    pythonPath: pythonPath,
    /* arg order: latitude,       longitude,      radiusMultiplier,     argv,       targetID */
    args: [req.body.longitude, req.body.latitude, req.body.number, req.body.query, req.body.ID],
  };

  PythonShell.run(pythonProcName, options, function (err, data) {
    if (err) {
      console.log('error on python process at ' + new Date().toString() + ': ' + err);
      res.json({ head: { error: "python process exception: " + parseErr(str(err)), }, res: {}, });
    } else {
      res.json(JSON.parse(data));
      if (requestFeedback) console.log(req.method + " response at " + new Date().toString() + ": " + data.toString().substring(0, 100));
    }
  });

});

app.listen(8090);

function parseErr(err) {
  trerr = err.substring(0, err.lastIndexOf("\n"));
  trerr = trerr.substring(trerr.lastIndexOf("\n") + 1);
  return trerr;
}
