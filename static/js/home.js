const button6 = document.querySelector('.button6')
const numfixid = document.querySelector('#numfixid')



button6 && button6.addEventListener('click' ,()=>{
    let choice1 = document.querySelectorAll('input[name="flexRadioDefault"]')
    choice1 = Object.values(choice1)
    const result1=choice1.filter(element1 => element1.checked ==true)[0];
    const content1 = result1.getAttribute('content');

    let choice2 = document.querySelectorAll('input[name="typeNumFac"]')
    choice2 = Object.values(choice2)
    const result2=choice2.filter(element2=>element2.checked==true)[0];
    const content2 = result2.getAttribute('content');

    let result = content1 + "/" + content2
    button6.setAttribute("href", result )

})
