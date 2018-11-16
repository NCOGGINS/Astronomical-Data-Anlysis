/*Test Object: Post Requests*/
function ajax(){
    var a = document.forms["myForm"]["A"].value;
    var formdata = {'a': a, 'b': 'thisisB'}; //read form requests into javascript object {'name': value, 'name': value, 'name': value}
    xmlhttp = new XMLHttpRequest(); //create new request each time

    xmlhttp.onreadystatechange=function(){ //onreadystatechange property fires each time the state changes, must be set to a function
      if(xmlhttp.readyState==4 && xmlhttp.status==200){
        document.getElementById("result").innerHTML=xmlhttp.responseText; //replace this line with what you want to do when the information is returned with a 200 (OK) code
      };
    };

    xmlhttp.open("POST","",true); //open POST request
    xmlhttp.setRequestHeader("Content-Type", "application/json"); //the server will not understand without it
    xmlhttp.send(JSON.stringify(formdata));
    return false;
  }
