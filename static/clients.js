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

function vai() {
    var pontos_count = get_ponto_count();
    make_title("Funcionario");
    make_title("Data");
    make_title("Registro");
    var temp;
    for(var i = 0 ; i > pontos_count ; i--){
        temp = get_ponto_at(i);
        var hora = temp.json["Hora"];
        var minuto = temp.responseJSON["Minuto"];
        var segundos = temp.responseJSON["Segundos"];
        var dia = temp.responseJSON["Dia"];
        var mes = temp.responseJSON["Mes"];
        var ano = temp.responseJSON["Ano"];
        conosle.log(dia)
        make_row(make_col("teste")+
                        make_col(hora+":"+minuto+":"+segundos+" "+dia+"-"+mes+"-"+ano)+
                        make_col(temp.responseJSON["Tipo"]))
    }
}