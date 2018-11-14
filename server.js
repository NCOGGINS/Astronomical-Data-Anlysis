/*
pythonProcName - path to python process relative to server.js
 */
var pythonProcName = "Test/SDSS.py";
console.log("starting...");

var url = require('url');
var express = require('express');
var app = express();
var path = require('path');
var webapp = path.join(__dirname, 'WebApp')

app.use(function (req, res, next) {
  console.log(req.method + " request at: " + new Date().toString());
  next();
});

app.use(express.static(webapp));

app.post('/*', function (req, res) {                        //wildcard * for testing
  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',[pythonProcName]); //[pythonProcName, argv1, argv2...]
  pythonProcess.stdout.on('data', (data) => {
    var txt = data.toString();
    res.json(JSON.parse(data));
    console.log(req.method + " response at: " + new Date().toString());
  });
})

app.listen(8090);
