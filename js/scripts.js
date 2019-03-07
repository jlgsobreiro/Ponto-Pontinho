document.getElementById("entra").onclick = function(){
	document.getElementById("div-ponto").className = "row scale-transition scale-in";
	document.getElementById("div-login").className = "scale-transition scale-out zero";
}

document.getElementById("cadastro").onclick = function(){
	document.getElementById("div-login").className = "scale-transition scale-out zero";
	document.getElementById("div-cadastrar").className = "row";
}

document.getElementById("cadastrar").onclick = function(){
	alert("Cadastro alguma coisa")
	document.getElementById("div-login").className = "row scale-transition scale-in";
	document.getElementById("top").className = "row top-menu";
	document.getElementById("div-cadastrar").className = "row hide";
}

document.getElementById("voltar").onclick = function(){
	document.getElementById("div-login").className = "row scale-transition scale-in";
	document.getElementById("top").className = "row top-menu";
	document.getElementById("div-cadastrar").className = "row hide";
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