var isDark = false

function darkMode(){
    if (isDark == false){
        document.querySelector("body").style.backgroundColor = "black"
        document.querySelector("main").style.backgroundColor = "#002d72"
        document.querySelector("main").style.color = "azure"
        isDark = true
    }else{
        document.querySelector("body").style.backgroundColor = "white"
        document.querySelector("main").style.backgroundColor = "azure"
        document.querySelector("main").style.color = "#002d72"
        isDark = false
    }
}

function reveal(){
    alert('Prefessor Keeleys | Web Authorship & Digital Media | CIT 231 | Autumn 2023 | 71000.202370');
}