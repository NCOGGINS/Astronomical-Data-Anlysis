//By: Nathan Coggins, Matthew Peek and KateLynn Pullen
//Last Modified 8 December 2018
//Project URL: http://66.191.217.115:8090

/*Test Object: Post Requests*/

var objIDIndex = 0;

/*
Called when the submit button for the form is clicked. Handles sending/receiving data.
 */
function ajax() {
    var query = document.forms["inputs"]["queryList"].value;
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
            console.log(xmlhttp.responseText);

            var string = JSON.parse(xmlhttp.responseText);
            var resultWindow = document.getElementById("resultWindow");

            if (string.head.error) { //if head.error exists, an error occurred
                makeError(string, resultWindow);
            } else if (string.head.type) {
                if (string.head.type.includes("num")) {
                    makeNum(string, resultWindow);
                }
                if (string.head.type.includes("scatterplot")) {
                    makeScatterplot(string, resultWindow);
                }
                if (string.head.type.includes("table")) {
                    makeTable(string, resultWindow);
                }
            }
        }
    };

    //xmlhttp.open("POST", "http://66.191.217.115:8090", true); /*this allows you to post the server from your own browser, in combination with CORS-disabled chrome shortcut "C:\path\to\chrome.exe" --disable-web-security --user-data-dir="C:/ChromeDevSession" */
    xmlhttp.open("POST", "", true); //open POST request
    xmlhttp.setRequestHeader("Content-Type", "application/json"); //the server will not understand without it
    xmlhttp.send(JSON.stringify(formdata));
    return false;
}

/*
Constructs a table from the response JSON, appends to resultWindow
@param string: response JSON, corresponds to string in ajax()
@param resultWindow: DOM element of div where results will be posted
 */
function makeTable(string, resultWindow) {
    // get the reference for the body
    var body = document.getElementsByTagName("body")[0];

    // creates a <table> element and a <tbody> element
    var tbl = document.createElement("table");
    var tblBody = document.createElement("tbody");

    var cols = string.res.columns.length;
    var rows = string.res.data.length;


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
        //classlists for scatterplot highlight feature
        row.classList.add("id" + string.res.data[i - 1][objIDIndex]);
        row.classList.add("row");
        //add function that fills ID field with clicked ID
        row.onclick = function () {
            document.forms["inputs"]["ID"].value = this.classList.item(0).substring(2);
        }
        for (var j = 0; j < cols; j++) {
            // Create a <td> element and a text node, make the text
            // node the contents of the <td>, and put the <td> at
            // the end of the table row
            var cell = document.createElement("td");
            var cellText = document.createTextNode(string.res.data[i - 1][j]);
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

/*
Alerts an error
@param string: response JSON, corresponds to string in ajax()
@param resultWindow: DOM element of div where results would be posted if not alert
 */
function makeError(string, resultWindow) {
    alert(string.head.error);
}

/*
Alerts a single numerical response (Object ID queries)
@param string: response JSON, corresponds to string in ajax()
@param resultWindow: DOM element of div where results would be posted if not alert
 */
function makeNum(string, resultWindow) {
  alert(string.res.data);
}

/*
Creates scatterplot from the response data, appends to resultWindow
@param string: response JSON, corresponds to string in ajax()
@param resultWindow: DOM element of div where results will be posted
 */
function makeScatterplot(string, resultWindow) {

    var data = string.res.data;
    var xAxisIndex = string.res.columns.indexOf(string.res.options.xAxis);
    var yAxisIndex = string.res.columns.indexOf(string.res.options.yAxis);
    var iAxis = [];
    if (string.res.options.iAxis) {
        for (var i = 0; i < string.res.options.iAxis.length; i++) {
            var temp = [];
            temp.push(string.res.options.iAxis[i]);
            temp.push(string.res.columns.indexOf(string.res.options.iAxis[i]));
            iAxis.push(temp);
        }
    }

    data = floatify(data, xAxisIndex);
    data = floatify(data, yAxisIndex);

    var margin = {top: 15, right: 15, bottom: 30, left: 50}
    , width = 800 - margin.left - margin.right
            , height = 600 - margin.top - margin.bottom;

    var x = d3.scaleLinear()
            .domain([d3.min(data, function (d) {
                    return d[xAxisIndex];
                }), d3.max(data, function (d) {
                    return d[xAxisIndex];
                })])
            .range([0, width]);

    var y = d3.scaleLinear()
            .domain([d3.min(data, function (d) {
                    return d[yAxisIndex];
                }), d3.max(data, function (d) {
                    return d[yAxisIndex];
                })])
            .range([height, 0]);

    var chart = d3.select('#' + resultWindow.id)
            .append('svg:svg')
            .attr('width', width + margin.right + margin.left)
            .attr('height', height + margin.top + margin.bottom)
            .attr('class', 'chart')

    var main = chart.append('g')
            .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
            .attr('width', width)
            .attr('height', height)
            .attr('class', 'main')

    // draw the x axis
    var xAxis = d3.axisBottom(x);

    main.append('g')
            .attr('transform', 'translate(0,' + height + ')')
            .attr('class', 'main axis date')
            .call(xAxis);

            //draw line at 300,000 if comparison to speed of light is requested in the response data
    if (string.res.options && string.res.options.misc && string.res.options.misc.includes("spd line")) {
        main.append("line")
                .attr("x1", 0)
                .attr("y1", y(300000))
                .attr("x2", width)
                .attr("y2", y(300000))
                .attr("stroke-width", 1)
                .attr("stroke", "red");
    }

    // draw the y axis
    var yAxis = d3.axisLeft(y);

    main.append('g')
            .attr('transform', 'translate(0,0)')
            .attr('class', 'main axis date')
            .call(yAxis);

    var g = main.append("svg:g");

    main.append("text")
        .attr("text-anchor", "end")
        .attr("x", width)
        .attr("y", height - 6)
        .text(string.res.columns[xAxisIndex]);

    main.append("text")
        .attr("text-anchor", "end")
        .attr("y", 6)
        .attr("dy", ".75em")
        .attr("transform", "rotate(-90)")
        .text(string.res.columns[yAxisIndex]);

    //construct tooltip
    var tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-10, 0])
            .html(function (d) {
                var str = "";
                for (var i = 0; i < iAxis.length; i++) {
                    str += iAxis[i][0].substring(7) + ": " + d[iAxis[i][1]] + "<br />";
                }
                str += "[" + d[xAxisIndex] + ", " + d[yAxisIndex] + "]";
                return str;
            });

    main.call(tip);

    g.selectAll("scatter-dots")
            .data(data)
            .enter().append("svg:circle")
            .attr("cx", function (d) {
                return x(d[xAxisIndex]);
            })
            .attr("cy", function (d) {
                return y(d[yAxisIndex]);
            })
            .attr("class", function (d) {
                return "id" + d[0] + " dot";
            })
            .style("fill-opacity", 0.75)
            .attr("r", 5)
            .style("fill", "black")
            .on("mouseover", tip.show)
            .on("mouseout", tip.hide)
            .on("click", highlightToggle);

}

/*
Switches all objects with "id[this ID NUMBER] dot" and "id[this ID NUMBER] row" to their highlighted
or unhighlighted forms, dependent on whether the original element clicked is currently
highlighted or not
@param this: hidden self pass from onclick
 */
function highlightToggle() {
    if (d3.select(this).attr("r") == 9) {
      d3.selectAll("." + this.classList.item(0) + ".dot")
              .style("fill-opacity", 0.75)
              .attr("r", 5)
              .style("fill", "black");
      d3.selectAll("." + this.classList.item(0) + ".row")
              .style("background-color", "whitesmoke");
    } else {
      d3.selectAll("." + this.classList.item(0) + ".dot")
              .style("fill-opacity", 1)
              .attr("r", 9)
              .style("fill", "orange");
      d3.selectAll("." + this.classList.item(0) + ".row")
              .style("background-color", "orange");
    }
}

/*
Parses every index'th field in a list of lists into a float. Used to ensure d3 can
parse max, min, x, and y locations properly.
@param list: list of lists
@param index: index to floatify
 */
function floatify(list, index) {
    for (var i = 0; i < list.length; i++) {
        list[i][index] = parseFloat(list[i][index]);
    }
    return list;
}

/*
Deletes all elements inside of resultWindow
 */
function clearResults() {
    document.getElementById("resultWindow").innerHTML = "";
}
