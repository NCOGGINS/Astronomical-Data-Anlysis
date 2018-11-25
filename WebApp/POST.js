//By: Nathan Coggins, Matthew Peek and KateLynn Pullen
//Last Modified 25 November 2018
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
        return "Not a query";
    }


    var latitude = document.forms["inputs"]["latitude"].value;
    var longitude = document.forms["inputs"]["longitude"].value;
    var number = document.forms["inputs"]["number"].value;
    var ID = document.forms["inputs"]["ID"].value;

    var formdata = {'query': query,
        'latitude': latitude,
        'longitude': longitude,
        'number': number,
        'ID': ID}; //read form requests into javascript object {'name': value, 'name': value, 'name': value}

    xmlhttp = new XMLHttpRequest(); //create new request each time

    xmlhttp.onreadystatechange = function () { //onreadystatechange property fires each time the state changes, must be set to a function
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            //console.log("It worked");
            console.log(xmlhttp.responseText);
            //document.getElementById("result").innerHTML = xmlhttp.responseText; //replace this line with what you want to do when the information is returned with a 200 (OK) code

        }
        ;
    };

    //xmlhttp.open("POST", "http://66.191.217.115:8090", true); /*this allows you to post the server from your own browser, in combination with CORS-disabled chrome shortcut "C:\path\to\chrome.exe" --disable-web-security --user-data-dir="C:/ChromeDevSession" */
    xmlhttp.open("POST", "", true); //open POST request
    xmlhttp.setRequestHeader("Content-Type", "application/json"); //the server will not understand without it
    xmlhttp.send(JSON.stringify(formdata));
    return false;
}
