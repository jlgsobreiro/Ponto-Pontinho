function arrive (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Inicio do expediente"})
    }))
}

function lunch_depart (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Saida para almoço"})
    }))
}

function lunch_arrive (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Volta do almoço"})
    }))
}

function depart (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Fim do expediente"})
    }))
}

function arriveBTN (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Inicio do expediente"})
    }))
}

function lunch_departBTN (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Saida para almoço"})
    }))
}

function lunch_arriveBTN (){
    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data, tipo : "Volta do almoço"})
    }))
}

function set_buttons (){
($.getJSON('/session',function (data,err){
        $.post('/last_entry',{user : data}, function ( last_entry ){
            var button = "btn-floating btn-large waves-effect waves-light"
            var yellow_disable = button + " yellow disable show"
            var grey_disable = button + " grey disable show"
            var green = button + " green show"
            var hide = button + " disable hide"
            if (last_entry == "Fim do expediente"){
                document.getElementById("arrive").className = (yellow_disable)
                document.getElementById("lunch_depart").className = (grey_disable)
                document.getElementById("lunch_arrive").className = (grey_disable)
                document.getElementById("depart").className = (grey_disable)
            }
            else if (last_entry == "Volta do almoço"){
                document.getElementById("arrive").className = (green)
                document.getElementById("lunch_depart").className = (green)
                document.getElementById("lunch_arrive").className = (green)
                document.getElementById("depart").className = (yellow_disable)
            }
            else if (last_entry == "Saida para almoço"){
               document.getElementById("arrive").className = (green)
                document.getElementById("lunch_depart").className = (green)
                document.getElementById("lunch_arrive").className = (yellow_disable)
                document.getElementById("depart").className = (grey_disable)
            }
            else if (last_entry == "Inicio do expediente"){
               document.getElementById("arrive").className = (green)
                document.getElementById("lunch_depart").className = (yellow_disable)
                document.getElementById("lunch_arrive").className = (grey_disable)
                document.getElementById("depart").className = (grey_disable)
            }
            else {
                document.getElementById("arrive").className = (yellow_disable)
                document.getElementById("lunch_depart").className = (grey_disable)
                document.getElementById("lunch_arrive").className = (grey_disable)
                document.getElementById("depart").className = (grey_disable)
            }
        })
    }))
}

$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('.collapsible').collapsible();
});

function callToast () {

}

function call_ponto(){
    if ($("#arrive").hasClass('yellow')){
        arrive()
    }
    else if ($("#lunch_depart").hasClass('yellow')){
        lunch_depart()
    }
    else if ($("#lunch_arrive").hasClass('yellow')){
        lunch_arrive()
    }
    else if ($("#depart").hasClass('yellow')){
        depart()
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