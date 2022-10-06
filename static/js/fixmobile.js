const button = document.querySelector('.button')
const button1 = document.querySelector('.button1')
const button5 = document.querySelector('.button5')


button.addEventListener("click",()=>{
    const inputNumFix = document.querySelector('#inputnum-fix')
    inputNumFix.setAttribute('type', 'file')
    button.setAttribute('hidden','true')
    button1.removeAttribute('hidden')

})




button1.addEventListener("click",()=>{
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

 