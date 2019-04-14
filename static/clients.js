
function make_col (item){
    return ("<td>"+item+"</td>")
}

function make_title (item){
    $("#head").append("<th>"+item+"</th>")
}

function make_row (item){
    return $("#tbody").append("<tr>"+item+"</tr>")
}

function get_all_pontos(){
    return $.getJSON("/get_all_pontos")
}

function get_ponto_at(index) {
    return $.getJSON("/get_ponto_at",{"index": index})
}

function get_ponto_count() {
    return $.getJSON("/get_ponto_count")
}

function get_user_name(user_id) {
    return $.getJSON("/get_user_name")
}

var pontos_count;
var ponto = null;
var nome;
$(document).ready(function(){
    $.ajaxSetup({
        async: false
    });
   pontos_count = parseInt(get_ponto_count().responseJSON);
   ponto = get_all_pontos();
   nome = get_user_name();
   $.ajaxSetup({
        async: true
    });
    make_title("Funcionario");
    make_title("Data");
    make_title("Registro");
     for(var i = 0 ; i < pontos_count ; i++){

        var hora = ponto.responseJSON[i]["Hora"];
        var minuto = ponto.responseJSON[i]["Minuto"];
        var segundos = ponto.responseJSON[i]["Segundos"];
        var dia = ponto.responseJSON[i]["Dia"];
        var mes = ponto.responseJSON[i]["Mes"];
        var ano = ponto.responseJSON[i]["Ano"];
        make_row(make_col(nome.responseJSON)+
                        make_col(hora+":"+minuto+":"+segundos+" "+dia+"-"+mes+"-"+ano)+
                        make_col(ponto.responseJSON[i]["Tipo"]))
    }

});


function vai() {
    pontos_count = get_ponto_count();



}