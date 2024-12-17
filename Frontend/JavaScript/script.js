// Understand the Basics

// 1. Variables
//Variables are Containers for Storing Data
console.log('Umer') // For Print
firstname = 'Umer'
lastname = 'toor'
console.log(firstname,lastname)
console.log(lastname)
hello = 'world'

// There are four ways of variables
// 2. let 
// 3. var 
// 4 . const

// Let 
let firstname1 = 'Ali'
console.log(firstname1)

var a,b,c  // Variable Initialize
a = 10  // Assign and Declare
b = 20
c = 30 
console.log(a+b+c)
// With let
let y = 20 
{
    let y = 50
    console.log('Body Scope', y)
}
console.log('After block body value Y ', y)

// Automatically 
 x = 20
{
    x = 40

}
console.log('After Block Scope Value', x)

// var
var z = 60 
{
    var z = 80
}
console.log('Value of z ', z)

// Const

const PI = 3.14

{
    const PI = 7.8
    
}
console.log(PI)