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


function myfunctionmobile(e){
    e.preventDefault()
    const form = e.target
    // console.log(form)
    let inpute = form["nameinput"];
    const tab = Object.values(inpute)
    let x = tab.filter(el => el.value != "")[0];
    console.log(x.value); 

    let radio = form["nameradio"];
    const rad = Object.values(radio)
    radio = rad.filter(elradio=> elradio.checked ==true)[0].getAttribute("value-content");
    console.log(radio);

    const year = form["year"].value;
    console.log(year);


    const month = form["month"].value;
    console.log(month);

}

async function myfunctionfixe(e){
    e.preventDefault()
    const form = e.target
    // console.log(form)
    let inpute = form["nameinput"];
    const tab = Object.values(inpute)
    let x = tab.filter(el => el.value != "")[0].value;

    console.log(x); 

    let radio = form["nameradio"];
    // console.log(radio);
    const rad2 = Object.values(radio)
    let radio1 = rad2.filter(elradio2=> elradio2.checked ==true)[0].getAttribute("value-content2");
    console.log(radio1);

    const year = form["year"].value;
    console.log(year);


    const month = form["month"].value;
    console.log(month);

    let data = {
        "univers": x,
        "type" : radio1,
        "mois" : month,
        "year" : year,
    }



    const response = await fetch("/apis", {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(data)
        });
    
        



}



// Factures = f'/fadet/factures/dossier_50877/{univers}/Fact/{annee}/{mois}/'
 
// Bordereau = f'/fadet/factures/dossier_50877/{univers}/Bord/pdf/{annee}/{mois}/'