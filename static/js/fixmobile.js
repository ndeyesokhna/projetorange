const button = document.querySelector('.button')
const button1 = document.querySelector('.button1')
const button5 = document.querySelector('.button5')


button && button.addEventListener("click",()=>{
    const inputNumFix = document.querySelector('#inputnum-fix')
    inputNumFix.setAttribute('type', 'file')
    button.setAttribute('hidden','true')
    button1.removeAttribute('hidden')

})




button1 && button1.addEventListener("click",()=>{
    const inputNumFix = document.querySelector('#inputnum-fix')
    inputNumFix.setAttribute('type', 'text')
    button1.setAttribute('hidden','true')
    button.removeAttribute('hidden')


})

function isKeyPressed(event) {
    var hide = document.querySelector("div.hide");
    if (event.metaKey) {
        hide.style.display="none"
    } else {
        hide.style.display="flex"
    }
  }

 
var hide1 = document.querySelector("div.hide1");
var hide3 = document.querySelector("div.hide3");

const names = window.location.pathname
const names1 = names.split("/");
// console.log(names1[2])

if(names1[2] == 'numcli'){
    // console.log(names1[2]);
    hide1.style.display="none"

}else{
    hide1.style.display="flex"
    hide3.style.display="none"

}

