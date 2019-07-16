$(document).ready(function(){
    var text = $.getJSON("/session", function (response){
        if ( response != "Off"){
            window.location.replace(window.location.href+"panel")
        }
    });

});
function access(){
    $.post("/login",{user:$('#username').val(),password:$('#password').val()},function(response){
        if(response["Access"] === "Granted") {
            window.location.replace(window.location.href+"panel")
        }
        if(response["Access"] === "Denied") {
            M.toast({html:"Senha ou login incorretos"})
        }
    })

}