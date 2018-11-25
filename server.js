/*
VARIABLES
pythonProcName - path to python process relative to server.js
staticLocation - path to index.html relative to server.js
requestFeedback - whether the server logs to console each time it receieves a request
 */
var pythonProcName = "Test/SDSS.py";
var staticLocation = "WebApp"; //change to "Test" to work with Test folder, "WebApp" otherwise
var requestFeedback = true;

/*
MODULES (dependencies)
 */
var url = require('url');
var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');

/**/

var app = express();
var webapp = path.join(__dirname, staticLocation)

app.use(bodyParser.json());

//potential security issue?
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header('Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS');
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
}); //TODO: remove when finished devl

app.use(function (req, res, next) {
  if (requestFeedback) console.log(req.method + " request at " + new Date().toString());
  next();
});

app.use(express.static(webapp));

app.post('*', function (req, res) {

  if (requestFeedback) console.log(req.method + " request contained: " + JSON.stringify(req.body));
  //latitude, longitude, radiusMultiplier, argv, targetID=None

  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',[pythonProcName, req.body.latitude, req.body.longitude, req.body.number, req.body.query, req.body.ID]); //[pythonProcName, argv1, argv2...]
  pythonProcess.stdout.on('data', (data) => {
    res.json(JSON.parse(data));
    if (requestFeedback) console.log(req.method + " response at " + new Date().toString() + ": " + data.toString().substring(0, 100));
  });

});

app.listen(8090);
