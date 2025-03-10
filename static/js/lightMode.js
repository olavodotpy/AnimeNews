let contador = 0;

const botaoModo = document.getElementById("darkMode");

botaoModo.addEventListener('click', function(){ 
    if (contador % 2 == 0) {
        
        document.body.style.background = "black";

        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = 'white';
        });
    }else{
        document.body.style.background = "white";
        
        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = 'black';
        });
    } 
    
    contador++;
});