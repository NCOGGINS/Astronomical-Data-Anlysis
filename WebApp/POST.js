//By: Nathan Coggins, Matthew Peek and KateLynn Pullen
//Last Modified 18 November 2018
//Project URL: http://66.191.217.115:8090

/*Test Object: Post Requests*/
function ajax() {
    var latitude = document.forms["inputs"]["latitude"].value;
    var longitude = document.forms["inputs"]["longitude"].value;
    var number = document.forms["inputs"]["number"].value;
    var ID = document.forms["inputs"]["ID"].value;

    var formdata = {'latitude': latitude,
        'longitude': longitude,
        'number': number,
        'ID': ID}; //read form requests into javascript object {'name': value, 'name': value, 'name': value}
    
    xmlhttp = new XMLHttpRequest(); //create new request each time

    xmlhttp.onreadystatechange = function () { //onreadystatechange property fires each time the state changes, must be set to a function
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            console.log("It worked");
            //document.getElementById("result").innerHTML = xmlhttp.responseText; //replace this line with what you want to do when the information is returned with a 200 (OK) code
            
        }
        ;
    };

    xmlhttp.open("POST", "", true); //open POST request
    xmlhttp.setRequestHeader("Content-Type", "application/json"); //the server will not understand without it
    xmlhttp.send(JSON.stringify(formdata));
    return false;
}
