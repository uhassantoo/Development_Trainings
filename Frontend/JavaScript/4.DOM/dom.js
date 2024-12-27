// Commonly Used DOM Methods
// Methods

// Description

// 1.  getElementById(id)
// Selects an element by its ID.

document.getElementById('p1').style.color = 'blue'

// 2. getElementsByClassName(class)

// Selects all elements with a given class.

let a = document.getElementsByClassName('div1')

a[1].style.backgroundColor = 'red'

//Tagname
function changebtn(){
    let ele = document.getElementById('div2')
    ele.getElementsByTagName('p')
    [1].style.fontSize = '36px'
}