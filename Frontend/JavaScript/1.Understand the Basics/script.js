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
let firstname1 = 'Ali h'
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

// ----------- Data Types ----------
// Primitive Data Types: They can hold a single simple value. String, Number, BigInt, Boolean, undefined, null, and Symbol are primitive data types.

let num = 123 // Number Data Type
let num1 = 11.23 // Number
let str = 'umer' // String
let bool = true // Boolean
let num2 = undefined // Undefiend


// The Object Datatype
// The object data type can contain both built-in objects, and user defined objects:

// Built-in object types can be:

// objects, arrays, dates, maps, sets, intarrays, floatarrays, promises, and more.

family_names = 'umer','hassan','hello'
console.log(family_names)

let arr = ['umer','hassan','toor']
console.log(arr)
let arr1 = ['age',12,true,null,12.2]
console.log(arr1)

let ages = ['Ali',20,'Ali1',22,'Ali2',25,'Ali3',28,'Ali4',30]
console.log(ages)
// Access Array
console.log(ages[4])
console.log(ages[8])

ages.push('total')
console.log(ages)
console.log(ages[10])

// Objects 
let names = {
    'ali' : 20,
    'ali1' : 22,
    'ali2' : 30,
    'ali3' : 42,

}
console.log(names)

names['ali3'] = ''
console.log(names)


// ---- Task Solution -----

let std_info = [
    {
         username: 'Umer', 
         age : 22,
         reg_num : 123 , 
         course : 'Programming', 
         fav_prog : ['HTML','JS','PYTHON','C++'],
         marks : {
            english : 90,
            urdu : 85,
            physics : 50,
            maths : 80,
         }
    },
    {
         username: 'Ali', 
         age : 24,
         reg_num : 1232 , 
         course : 'Programming', 
         fav_prog : ['HTML','JS','PYTHON','C++'],
         marks : {
            english : 94,
            urdu : 84,
            physics : 50,
            maths : 80,
         }
    }
]

console.log(std_info)
console.log(std_info[1].username)
console.log(std_info[1].age)

// ---Marks---
console.log(std_info[1].marks.english)