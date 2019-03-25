function callToast () {
    if (document.getElementById('errado')){
        M.toast({html: 'I am a toast!'});
    }
}

<<<<<<< HEAD
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });
=======
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
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823

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
<<<<<<< HEAD
<<<<<<< HEAD

function callToast (){

     M.toast({html: 'I am a toast!', classes: 'rounded'});

}
=======
>>>>>>> 1f4f45398ef1ecba7a392200cdb5d8e74a81be9b
=======
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823
