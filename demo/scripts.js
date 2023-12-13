var isDark = false

function darkMode() {
    if (isDark == false){
        document.querySelector("body").style.backgroundColor = "black"
        document.querySelector("body").style.color = "lightblue"
        isDark = true
    }else{
        document.querySelector("body").style.backgroundColor = "white"
        document.querySelector("body").style.color = "blue"
        isDark = false
    }
    
}