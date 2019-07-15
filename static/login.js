$(document).ready(function(){
    if ( $.getJSON("/session") != "Off"){
        window.location.replace(window.location.href+"panel")
    }

});
function access(){

    $.post("/login",{user:$('#username').val(),password:$('#password').val()},function(response){
        if(response["Access"] === "Granted")
            window.location.replace(window.location.href+"panel")
    })

}