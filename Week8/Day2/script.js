// let b = 3, d = b, u = b;

// const tree = ++d * d*b * b++ +
// + --d+ + +b-- +
// + +d*b+ +
// u

// console.log(tree); //163

// 4 * 4 * 3 * 3 
// + 3 + 4 +
// 3 * 3 +
// 3

// // /*variable scoup*/
// // var a =3;
// // let b = 5;
// // const D = 7;

// /*Functions*/
// function getName(param1, param2){
//     console.log(param1, param2)
// }
// getName('Marry', 'John')

// /*Exercise1*/

// function getAge(myAge){
//     let mum = myAge*2
//     let dad = mum*1.2
//     return [dad, mum]
// }

// res = getAge(23)
// console.log(res)

// ?Exercise 1: Traversing the DOM
// Knowing how to traverse the DOM using JavaScript provides a foundation
// to altering an HTML page in real time.
// Using the HTML markup in Listing 1, perform these tasks:
// 1. Use the firstElementChild  property to access an element.+
// 2. Use the lastElementChild   property to access an element.+
// 3. Use the nextElementSibling   property to access an element.
// 4. Use the previousElementSibling   property to access an element.
// 5. Use the parentNode property to access an element.
// 6. Use the childNodes property to access a group of child elements.

// Exercise 2: Targeting nodes 
// In exercise 1, you learned how to target nodes in several ways.
// Continuing to use the markup in Listing 1, perform the following tasks:
// 1. Retrieve the value of a node using / innerText / innerHTML.
// 2. Change the value of a node using / innerText / innerHTML.
// 3. Retrieve the value of a node attribute.
// 4. Change the value of a node attribute.

// Exercise 3: Manipulating the DOM
// Now that you know how to traverse the DOM and alter node values,
// the next logical step is to learn how to add, remove, and replace nodes.
// Perform the following tasks:
// 1. Use the appendChild method to add a node.
// 2. Use the insertBefore method to add a node.
// 3. Use the removeChild method to remove a node.
// 4. Use the replaceChild method to replace a node.

const parentElement = document.getElementById("page");
const first = parentElement.firstElementChild;
console.log(first)
const last = parentElement.lastElementChild;
console.log(last)

console.log(first)
const fsibl = first.nextElementSibling;
console.log(fsibl)


