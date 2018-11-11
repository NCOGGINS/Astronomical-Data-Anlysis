/*
pythonProcName - change to ./SDSSQuery/whatever when you want to test
 */
var pythonProcName = "temp.py";
console.log("starting...");

var url = require('url');
var express = require('express');
var app = express();
var path = require('path');

app.get('/', function (req, res) {

  res.sendFile('WebApp/index.html', {root : __dirname});

  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',[pythonProcName]); //[pythonProcName, argv1, argv2...]
  pythonProcess.stdout.on('data', (data) => {
    var txt = data.toString();
    console.log("response from python process: ") //test
    console.log(txt);
  });

})

app.listen(8090);
