var lista_de_tipo_de_ponto = ["Inicio do expediente",
                                "Saida para almoço",
                                "Volta do almoço",
                                "Fim do expediente"]

function last_ponto_arrive( ){
    $.post('/last_ponto',{last : lista_de_tipo_de_ponto[0]}, function ( response ){
        $("#last_time_registry").html(response)
    })
}

function last_ponto_lunch_depart( ){
    $.post('/last_ponto',{last : lista_de_tipo_de_ponto[1]}, function ( response ){
        $("#last_time_registry").html(response)
    })
}

function last_ponto_lunch_arrive( ){
    $.post('/last_ponto',{last : lista_de_tipo_de_ponto[2]}, function ( response ){
        $("#last_time_registry").html(response)
    })
}

function last_ponto_depart( ){
    $.post('/last_ponto',{last : lista_de_tipo_de_ponto[3]}, function ( response ){
        $("#last_time_registry").html(response)
    })
}
function arrive (){
    $.post('/arrive',{tipo : lista_de_tipo_de_ponto[0]})
}

function lunch_depart (){
    $.post('/arrive',{tipo : lista_de_tipo_de_ponto[1]})
}

function lunch_arrive (){
    $.post('/arrive',{tipo : lista_de_tipo_de_ponto[2]})
}

function depart (){
    $.post('/arrive',{tipo : lista_de_tipo_de_ponto[3]})
}

function set_buttons (){
    $.post('/last_entry', function ( last_entry ){
        var button = "btn-floating btn-large waves-effect waves-light"
        var yellow_disable = button + " yellow disable show"
        var grey_disable = button + " grey disable show"
        var green = button + " green show"
        var hide = button + " disable hide"
        if (last_entry == lista_de_tipo_de_ponto[3]){
            document.getElementById("arrive").className = (yellow_disable)
            document.getElementById("lunch_depart").className = (grey_disable)
            document.getElementById("lunch_arrive").className = (grey_disable)
            document.getElementById("depart").className = (grey_disable)
        }
        else if (last_entry == lista_de_tipo_de_ponto[2]){
            document.getElementById("arrive").className = (green)
            document.getElementById("lunch_depart").className = (green)
            document.getElementById("lunch_arrive").className = (green)
            document.getElementById("depart").className = (yellow_disable)
        }
        else if (last_entry == lista_de_tipo_de_ponto[1]){
            document.getElementById("arrive").className = (green)
            document.getElementById("lunch_depart").className = (green)
            document.getElementById("lunch_arrive").className = (yellow_disable)
            document.getElementById("depart").className = (grey_disable)
        }
        else if (last_entry == lista_de_tipo_de_ponto[0]){
            document.getElementById("arrive").className = (green)
            document.getElementById("lunch_depart").className = (yellow_disable)
            document.getElementById("lunch_arrive").className = (grey_disable)
            document.getElementById("depart").className = (grey_disable)
        } else {
                document.getElementById("arrive").className = (yellow_disable)
                document.getElementById("lunch_depart").className = (grey_disable)
                document.getElementById("lunch_arrive").className = (grey_disable)
            document.getElementById("depart").className = (grey_disable)
        }
    })
}

function call_ponto(){
    if ($("#arrive").hasClass('yellow')){
        arrive()
        set_buttons();
    }
    else if ($("#lunch_depart").hasClass('yellow')){
        lunch_depart()
        set_buttons();
    }
    else if ($("#lunch_arrive").hasClass('yellow')){
        lunch_arrive()
        set_buttons();
    }
    else if ($("#depart").hasClass('yellow')){
        depart()
        set_buttons();
    }
    set_buttons()
}


function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  // add a zero in front of numbers<10
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('tempo-real').innerHTML = h + ":" + m + ":" + s;
  t = setTimeout(function() {
    startTime()
  }, 500);
}
startTime();
set_buttons();