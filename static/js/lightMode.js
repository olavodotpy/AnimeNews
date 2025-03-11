const lightmode = document.getElementById("lightmode");

let count = 0;

lightmode.addEventListener('click', function(){ 
    if (count % 2 == 0) {
        
        document.documentElement.style.setProperty('--bodybackg', '#0B0E11');
        document.documentElement.style.setProperty('--bodycolor', '#f7f7f7');

        document.documentElement.style.setProperty('--backg-button-home', '#0B0E11');
        document.documentElement.style.setProperty('--color-button-home', '#f7f7f7');

        document.documentElement.style.setProperty('--card-backg', '#191919');
        document.documentElement.style.setProperty('--card-info-color', '#ffffff');

        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = '#ffffff';
        });
    }else{

        document.documentElement.style.setProperty('--bodybackg', '#f7f7f7');
        document.documentElement.style.setProperty('--bodycolor', '#0e0e0e');

        document.documentElement.style.setProperty('--backg-button-home', '#f7f7f7');
        document.documentElement.style.setProperty('--color-button-home', '#0e0e0e');

        document.documentElement.style.setProperty('--card-backg', '#ffffff');
        document.documentElement.style.setProperty('--card-info-color', '#0e0e0e');
        
        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = '#000';
        });
    } 
    
    count++;
});