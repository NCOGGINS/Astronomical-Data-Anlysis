/*Test Object: Post Requests*/
function ajax(){
    var a = document.forms["myForm"]["A"].value;
    var formdata = a;
    xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange=function(){
      if(xmlhttp.readyState==4 && xmlhttp.status==200){
        document.getElementById("result").innerHTML=xmlhttp.responseText;
      };
    };

    xmlhttp.open("POST","",true);
    xmlhttp.send(formdata);
    return false;
  }
