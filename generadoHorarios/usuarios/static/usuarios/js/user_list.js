$(function(){
    $('.btnTest').on('click',function(){
        $.ajax({
            url: '{% url 'usuarios:administradores' %}',
            type: 'POST',
            data: {id:1212},
            dataType: 'json'
        }).done(function(data){
            console.log(data);
        }).fail(function(jqXHR,textStatus,errorThrown){
            alert(textStatus+': '+errorThrown);
        }).always(function(data){

        })
    })
})