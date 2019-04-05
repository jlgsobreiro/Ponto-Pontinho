function access(){

    $.post("/login",{user:123,password:123},function(response){
        if(response["Access"] == "Granted")
            window.location.replace(window.location.href+"panel")
    })

}