// // 
//  Control structures are programmatic constructs that determine how your code executes. They provide mechanisms for making decisions, repeating code blocks, and changing the flow of execution based on specific conditions. 
// Conditional Statements: 

console.log('Persons Age')
person1 = 33 
person2 = 33
if(person1<person2) // true
    {
   console.log('Person 2 is greater')
 
}
else if(person1>person2)
{
    console.log('Person 1 is greater')
}
else 
{
    console.log('Person 1 is smaller')
}



let grade = 40
if(grade>= 90){
    console.log('Execlent')
}
else if (grade>=80 && grade>=89){
    console.log('VGood')
}
else if (grade>=60 && grade>=79)
{
    console.log('Good')
}
else if (grade>=50 && grade>=59)
{
    console.log('Passed')
}
else 
{
    console.log('Fail')
}

// Switch Statement

let days = 'Tuesday'

switch (days) {
    case 'Monday':  // if
        console.log('Today is Monday')
        break;
    case 'tuesday': // else if
        console.log('Today is Tuesday')
        break;

    default:  // else
    console.log('Weekend')
        break;
}

// Task  Grade Program should be in Switch Statement



// Ternary Operator
ages = 14
let message = ages >= 18 ?  'You are eligible for voting' : 'Not eligible'
console.log(message)