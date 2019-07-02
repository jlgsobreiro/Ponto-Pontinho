function register(){

    $.post("/register",{username:$('usuario').val(),
            password:$('senha').val(),
            confirm_password:$('confirma_senha').val(),
            email:$('email').val(),
            name:$('nome').val(),
            last_name:$('sobrenome').val()},
            function(response){
                if(response["Register"] === "Granted")
                    window.location.replace(window.location.href+"panel")
    })

}