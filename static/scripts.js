function callToast () {
    if (document.getElementById('errado')){
        M.toast({html: 'I am a toast!'});
    }
}

function arrive (){

    ($.getJSON('/session',function teste(data,err){
        $.post('/arrive',{user : data })
        console.log(data)
    }))


}

function lunch_depart (){


}

function lunch_arrive (){


}

function depart (){


}

$(document).ready(function(){
    $('.sidenav').sidenav();
});

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
