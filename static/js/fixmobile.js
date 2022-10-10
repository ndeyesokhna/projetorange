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
    console.log(event.target);
    var hide = document.querySelector("div.hide");
    var hide8 = document.querySelector("div.hide8");
    var hiden3 = document.querySelector("div.hiden3");
    const parent = event.target.parentElement.parentElement
    const divFF = parent.querySelector('.FF')
    if (event.metaKey) {
        hiden3.style.display="none"
        // hide8.style.display="flex"
        divFF.style.display="flex"
        console.log(hfvh)
    } else {
        hiden3.style.display="flex"
        // hide8.style.display="none"
        divFF.style.display="flex"

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





