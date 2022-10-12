let footer = document.querySelector("footer")
let form = document.querySelector("form")

function insertAfter(newNode, existingNode) {
    existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}

insertAfter(footer,  form);