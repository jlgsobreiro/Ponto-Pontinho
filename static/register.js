
$("#cadastrar").click(function() {
    $.post("/register",{username:$('#username').val(),
        password:$('#password').val(),
        confirm_password:$('#confirm_password').val(),
        email:$('#email').val(),
        name:$('#name').val(),
        last_name:$('#last_name').val()}, function(response){
            console.log(response)
            if(response["Register"] === "Registered")
                window.location.replace(window.location.href+"panel")
            })
});

$("#voltar").click(function() {
    window.location.replace(window.location.href+"/")
});