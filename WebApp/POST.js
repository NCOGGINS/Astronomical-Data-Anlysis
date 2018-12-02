//By: Nathan Coggins, Matthew Peek and KateLynn Pullen
//Last Modified 1 December 2018
//Project URL: http://66.191.217.115:8090

/*Test Object: Post Requests*/
function ajax() {
    if (document.forms["inputs"]["queryList"].value === "view query results") {
        var query = 0;
    } else if (document.forms["inputs"]["queryList"].value === "view spectra results") {
        var query = 1;
    } else if (document.forms["inputs"]["queryList"].value === "receding velocity") {
        var query = 2;
    } else if (document.forms["inputs"]["queryList"].value === "object speed light percent") {
        var query = 3;
    } else if (document.forms["inputs"]["queryList"].value === "lum distance") {
        var query = 4;
    } else if (document.forms["inputs"]["queryList"].value === "plot magnitudes") {
        var query = 5;
    } else {
        console.log("Not a query!");
        var query = -1;
    }


    var latitude = document.forms["inputs"]["latitude"].value;
    var longitude = document.forms["inputs"]["longitude"].value;
    var number = document.forms["inputs"]["radius"].value;
    var ID = document.forms["inputs"]["ID"].value;

    var formdata = {'query': query,
        'latitude': latitude,
        'longitude': longitude,
        'number': number,
        'ID': ID}; //read form requests into javascript object {'name': value, 'name': value, 'name': value}

    xmlhttp = new XMLHttpRequest(); //create new request each time

    xmlhttp.onreadystatechange = function () { //onreadystatechange property fires each time the state changes, must be set to a function
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            //console.log("It worked");
            console.log(xmlhttp.responseText);

            var string = JSON.parse(xmlhttp.responseText);
            var resultWindow = document.getElementById("resultWindow");

            if (string.head.type.includes("table")) {
              makeTable(string, resultWindow);
            }
            if (string.head.type.includes("num")) {
              makeNum(string, resultWindow);
            }
            if (string.head.type.includes("scatterplot")) {
              makeScatterplot(string, resultWindow);
            }
        }
    };

    //xmlhttp.open("POST", "http://66.191.217.115:8090", true); /*this allows you to post the server from your own browser, in combination with CORS-disabled chrome shortcut "C:\path\to\chrome.exe" --disable-web-security --user-data-dir="C:/ChromeDevSession" */
    xmlhttp.open("POST", "", true); //open POST request
    xmlhttp.setRequestHeader("Content-Type", "application/json"); //the server will not understand without it
    xmlhttp.send(JSON.stringify(formdata));
    return false;
}


function makeTable(string, resultWindow) {
  // get the reference for the body
  var body = document.getElementsByTagName("body")[0];

  // creates a <table> element and a <tbody> element
  var tbl = document.createElement("table");
  var tblBody = document.createElement("tbody");

  var cols = string.res.columns.length;
  var rows = string.res.data[0].length;


  //Create header row from column names
  var row = document.createElement("tr");
  for (var i = 0; i < cols; i++) {
      var cell = document.createElement("td");
      var cellText = document.createTextNode(string.res.columns[i]);
      cell.appendChild(cellText);
      row.appendChild(cell);
  }
  tblBody.appendChild(row);

  // creating all cells
  for (var i = 1; i < rows + 1; i++) {
      // creates a table row
      var row = document.createElement("tr");

      for (var j = 0; j < cols; j++) {
          // Create a <td> element and a text node, make the text
          // node the contents of the <td>, and put the <td> at
          // the end of the table row
          var cell = document.createElement("td");
          var cellText = document.createTextNode(string.res.data[j][i - 1]);
          cell.appendChild(cellText);
          row.appendChild(cell);
      }

      // add the row to the end of the table body
      tblBody.appendChild(row);
  }

  // put the <tbody> in the <table>
  tbl.appendChild(tblBody);
  // appends <table> into <body>
  body.appendChild(tbl);
  // sets the border attribute of tbl to 2;
  tbl.setAttribute("border", "2");

  resultWindow.appendChild(tbl);
}

function makeNum(string, resultWindow) {

}

function makeScatterplot(string, resultWindow) {

}
