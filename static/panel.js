login_url = '127.0.0.1:5000/'
function load_ponto(){
    $("#container").load("/ponto")
}
function load_historico_ponto(){
    $("#container").load("/historico_ponto")
}
function load_clients(){
    $("#container").load("/clients")
}

function load_production(){
    $("#container").load("/production")
}

function load_expedition(){
    $("#container").load("/expedition")
}

function load_routes(){
    $("#container").load("/routes")
}

function load_employees(){
    $("#container").load("/employees")
}
function get_user_name() {
    return $.getJSON("/get_user_name")
}

$('#logoff').click(function(){
    console.log("Saindo")
    $.post("/logoff",function(response){
        if(response["Session"] === "Cleared")
            window.location.replace(login_url)
    })
})

$.getJSON('/session',function (data,err){
            var d = new Date();
            var n = d.getHours();
            if(n>=12){
                $("#welcome").html("Boa tarde "+data+"!")
            } else if(n>=18){
                $("#welcome").html("Boa noite "+data+"!")
            } else {
                $("#welcome").html("Bom dia "+data+"!")
            }
        })