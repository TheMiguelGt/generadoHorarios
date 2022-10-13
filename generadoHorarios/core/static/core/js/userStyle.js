// ejecutar funcion en el evento click
document.getElementById("btn_open").addEventListener("click", open_close_menu);

var side_menu = document.getElementById("menu__side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");

// eventos para mostrar y ocultar
function open_close_menu(){
    body.classList.toggle("body_move");
    side_menu.classList.toggle("menu__side_move");
}

// si el ancho es menor a 760px ocultara el menu al recargar la pagina 
if(window.innerWidth < 760){
    body.classList.add("body_move");
    side_menu.classList.add("menu__side_move");
}
// haciendo el menu responsive
window.addEventListener("resize", function(){
    if(window.innerWidth > 760){
        body.classList.remove("body_move");
        slide_menu.classList.remove("menu__side_move");
    }
    if(window.innerWidth < 760){
        body.classList.add("body_move");
        side_menu.classList.add("menu__side_move");
    }
})