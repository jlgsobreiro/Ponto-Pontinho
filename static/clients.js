function make_col (item){
    return ("<td>"+item+"</td>")
}

function make_title (item){
    $("#head").append("<th>"+item+"</th>")
}

function make_row (item){
    return ("<tr>"+item+"</tr>")
}

function get_all_pontos(){
    $.getJSON("/get_all_pontos", function (data) {
        return data
    })
}

function get_ponto_count() {
    $.getJSON("/get_ponto_count", function (count) {
        return count
    })
}

$(document).ready(function() {

    $.each(get_all_pontos(),function (colindex, text) {

    })
});