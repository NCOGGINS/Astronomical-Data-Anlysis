/*
pythonProcName - change to ./SDSSQuery/whatever when you want to test
 */
var pythonProcName = "temp.py";
console.log("starting...");

var http = require('http');
var url = require('url');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});


  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',[pythonProcName]); //[pythonProcName, argv1, argv2...]
  pythonProcess.stdout.on('data', (data) => {
    var txt = data.toString();
    res.end(txt);
  });

}).listen(8090);
