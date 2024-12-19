// JavaScript Operator Types
// Here is a list of different JavaScript operators you will learn in this tutorial:

// Arithmetic Operators
// Assignment Operators
// Comparison Operators
// Logical Operators


// Arithmetic Operator  +,-,*,/,%

let num1,num2
let add,sub,mul,div,mod 

num1 = 50
num2 = 30
add = num1 + num2
console.log(add)

sub = num1 - num2 
console.log(sub)

mul = num1 * num2
console.log(mul)

div = num1/num2
console.log(div)

mod = num1 % num2
console.log(mod)

num1++ // num1 = num1 + 1
console.log(num1)

num2--
console.log(num2)

exp = num1 ** num2
console.log(exp)

// Assignment Operators

num1 += 5 // num1 = num1 + 5
console.log(num1)

// Comparison Operators

// We use comparison operators to compare two values and return a boolean value (true or false). 

let a = 20
let b = 40 
console.log(a<b) // True
console.log(a>b) // False
console.log(a<=b) // true
console.log(a>=b)// False

// Logical Operators
console.log('Logical Operator')
console.log((a<=b) && (a>=b))
console.log((a<=b) || (a>=b))
console.log(!(a<=b) && (a>=b))