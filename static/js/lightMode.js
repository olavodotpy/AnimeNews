const lightmode = document.getElementById("lightmode");
const imgLightMode = document.querySelector("#imgMode")

let count = 0;


lightmode.addEventListener('click', function(){ 
    if (count % 2 == 0) {
        
        document.documentElement.style.setProperty('--color-backg', '#191c20');
        document.documentElement.style.setProperty('--color', '#f7f7f7');
        imgLightMode.setAttribute("src", "/static/image/brightness_light.png")
        
        document.documentElement.style.setProperty('--card-backg', '#191919');
        document.documentElement.style.setProperty('--card-info-color', '#ffffff');

        const font_elementos = document.querySelectorAll(".text_color");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = '#ffffff';
        });
    }else{

        document.documentElement.style.setProperty('--color-backg', '#f7f7f7');
        document.documentElement.style.setProperty('--color', '#0e0e0e');
        imgLightMode.setAttribute("src", "/static/image/brightness_dark.png")

        document.documentElement.style.setProperty('--card-backg', '#ffffff');
        document.documentElement.style.setProperty('--card-info-color', '#0e0e0e');
        
        const font_elementos = document.querySelectorAll(".text_color");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = '#000';
        });
    } 
    
    count++;
});