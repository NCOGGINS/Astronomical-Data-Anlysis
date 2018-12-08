//By: Nathan Coggins, Matthew Peek and KateLynn Pullen
//Last Modified 8 December 2018
//Project URL: http://66.191.217.115:8090

/*Test Object: Post Requests*/

var objIDIndex = 0;

function ajax() {
    if (document.forms["inputs"]["queryList"].value === "View query results") {
        var query = 0;
    } else if (document.forms["inputs"]["queryList"].value === "View spectra results") {
        var query = 1;
    } else if (document.forms["inputs"]["queryList"].value === "Receding velocity") {
        var query = 2;
    } else if (document.forms["inputs"]["queryList"].value === "Object speed light percentage (EXPERIMENTAL FEATURE)") {
        var query = 3;
    } else if (document.forms["inputs"]["queryList"].value === "Luminosity distance (EXPERIMENTAL FEATURE)") {
        var query = 4;
    } else if (document.forms["inputs"]["queryList"].value === "Plot magnitudes") {
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

            if (string.head.error) { //if head.error exists, an error occurred
                makeError(string, resultWindow);
            } else if (string.head.type) {
                if (string.head.type.includes("num")) {
                    makeNum(string, resultWindow);
                }
                if (string.head.type.includes("scatterplot")) {
                    makeScatterplot(string, resultWindow);
                    clearHighlight();
                }
                if (string.head.type.includes("table")) {
                    makeTable(string, resultWindow);
                }
            }
        }
    };

    xmlhttp.open("POST", "http://66.191.217.115:8090", true); /*this allows you to post the server from your own browser, in combination with CORS-disabled chrome shortcut "C:\path\to\chrome.exe" --disable-web-security --user-data-dir="C:/ChromeDevSession" */
    //xmlhttp.open("POST", "", true); //open POST request
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
        row.classList.add("id" + string.res.data[i - 1][objIDIndex]);
        row.classList.add("row");
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

function makeError(string, resultWindow) {
    document.getElementById("resultWindow").innerHTML += string.head.error.toString();
}

function makeNum(string, resultWindow) {

}

function makeScatterplot(string, resultWindow) {

    var data = string.res.data; //do something with string
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


    //http://bl.ocks.org/bunkat/2595950

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
            .on("mouseover", tip.show)
            .on("mouseout", tip.hide)
            .on("click", highlight);

}

function highlight() {
    d3.selectAll("." + this.classList.item(0) + ".dot")
            .style("fill-opacity", 1)
            .attr("r", 9)
            .style("fill", "orange");
    d3.selectAll("." + this.classList.item(0) + ".row")
            .style("background-color", "orange");
}

function clearHighlight() {
    d3.selectAll(".dot")
            .style("fill-opacity", 0.75)
            .style("fill", "black")
            .attr("r", 5);
    d3.selectAll(".row")
            .style("background-color", "auto");
}

function floatify(list, index) {
    for (var i = 0; i < list.length; i++) {
        list[i][index] = parseFloat(list[i][index]);
    }
    return list;
}

function clearResults() {
    document.getElementById("resultWindow").innerHTML = "";
}