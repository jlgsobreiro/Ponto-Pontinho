//Faz coluna
function make_col (item){
    return ("<td>"+item+"</td>")
}
//Cria titulo da coluna
function make_title (item){
    $("#head").append("<th>"+item+"</th>")
}
//Cria linha
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

function get_user_name() {
    return $.getJSON("/get_user_name")
}

var pontos_count;
var ponto = null;
var nome;
$(document).ready(function(){
    $('.fixed-action-btn').floatingActionButton();
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

        var hora = ponto.responseJSON[i]["Horario"];
        var dia_semana = ponto.responseJSON[i]["Dia_semana"];
        var dia = ponto.responseJSON[i]["Dia"];
        var mes = ponto.responseJSON[i]["Mes"];
        var ano = ponto.responseJSON[i]["Ano"];
        make_row(make_col(nome.responseJSON)+
                        make_col(dia_semana+" "+dia+"-"+mes+"-"+ano+" "+hora)+
                        make_col(ponto.responseJSON[i]["Tipo"]))
    }

});
