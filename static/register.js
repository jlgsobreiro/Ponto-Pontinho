login_url = 'http://127.0.0.1:5000/'

function isEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

$( "#email" ).keypress(function( event ) {
  if(isEmail($("#email").val())){
        console.log(isEmail($("#email").val()))
        $("#email").css("validate valid");
    } else {
        $("#email").css("validate invalid");
    }
});


$("#cadastrar").click(function() {
    $.post("/register",{username:$('#username').val(),
        password:$('#password').val(),
        confirm_password:$('#confirm_password').val(),
        email:$('#email').val(),
        name:$('#name').val(),
        last_name:$('#last_name').val()}, function(response){
            console.log(response)
            if(response["Register"] === "Registered"){
                M.toast({html: 'Usuario registrado com sucesso',
                     completeCallback: function(){
                        window.location.replace(login_url)
                      }
                 })
            } else if (response["Register"] === "Name"){
                if (!($("#name").hasClass("invalid"))){
                    $("#name").toggleClass("invalid");
                }
                M.toast({html: "Preencha o campo Nome"})
            } else if (response["Register"] === "Last_name"){
                if (!($("#last_name").hasClass("invalid"))){
                    $("#last_name").toggleClass("invalid");
                }
                M.toast({html: "Preencha o campo Sobrenome"})
            } else if (response["Register"] === "Username"){
                if (!($("#username").hasClass("invalid"))){
                    $("#username").toggleClass("invalid");
                }
                M.toast({html: "Preencha o campo Usuário"})
            } else if (response["Register"] === "Email"){
                if (!($("#email").hasClass("invalid"))){
                    $("#email").toggleClass("invalid");
                }
                M.toast({html: "Email invalido"})
            } else if (response["Register"] === "Password"){
                if (!($("#password").hasClass("invalid"))){
                    $("#password").toggleClass("invalid");
                }
                M.toast({html: "Preencha o campo Senha"})
            } else if (response["Register"] === "Confirm_password"){
                if (!($("#confirm_password").hasClass("invalid"))){
                    $("#confirm_password").toggleClass("invalid");
                }
                M.toast({html: "Preencha o campo Confirma Senha"})
            } else if (response["Register"] === "Not_equal"){
                if (!($("#confirm_password").hasClass("invalid"))){
                    $("#confirm_password").toggleClass("invalid");
                }
                if (!($("#password").hasClass("invalid"))){
                    $("#password").toggleClass("invalid");
                }
                M.toast({html: "Senhas não batem"})
            } else if (response["Register"] === "Exists"){
                if (!($("#username").hasClass("invalid"))){
                    $("#username").toggleClass("invalid");
                }
                M.toast({html: "Ususario já existe"})
            }
        }
    )
});

$("#voltar").click(function() {
    window.location.replace(login_url)
});
