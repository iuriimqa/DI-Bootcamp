// // Exercise1

// // 1.Using a DOM property, retrieve the h1 and console.log it.


// const h = document.querySelector('h1')
// let number = Math.floor(Math.random() * 100)
// h.addEventListener('mouseover',() => {
//     h.style.fontSize = number + 'px';
// })
// console.log('h1:',h);

// // 2.Using DOM methods, remove the last paragraph in the <article> tag.

// const article = document.querySelector('article');
// const lastPr = article.lastElementChild;
// lastPr.remove();
// console.log("article:",article)

// // 3.Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// const h2 = document.querySelector('h2');
// h2.addEventListener('click', () => {
//     h2.style.backgroundColor = 'red';
//   });

// //   4.Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// const h3 = document.querySelector('h3');
// h3.addEventListener('click',() => {
//     h3.style.setProperty('display', 'none');
// });

// // 6.BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100
// // in 1st section

// // Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// function makeParagraphsBold() {
//     const paragraphs = document.querySelectorAll('p');
//     for (const paragraph of paragraphs) {
//       paragraph.style.fontWeight = 'bold';
//     }
//   }

// // 7. When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

// const PRGRAPH = document.getElementById('second');
// PRGRAPH.addEventListener('mouseover', () => {
//   PRGRAPH.style.setProperty('opacity', '0');
// });


/*Exercise2*/
// 1.Retrieve the form and console.log it.

// const form = document.querySelector('form');
// console.log(form);

// // 2.Retrieve the inputs by their id and console.log them.
// const firstName = document.getElementById("fname")
// const lastName = document.getElementById('lname')
// const submit = document.getElementById('submit')

// console.log(firstName, lastName, submit);

// 3.Retrieve the inputs by their name attribute and console.log them.
// const form = document.querySelector("form");
// const firstName = document.querySelector("[name = fname]");
// const lastName = document.querySelector("[name = lname]");
// const button = document.getElementById('submit');

// console.log(form,firstName, lastName);

// 4.When the user submits the form (ie. submit event listener)

// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// // then append them to a the <ul class="usersAnswer"></ul>, below the form.

// const form = document.querySelector("form");
// const firstName = document.querySelector("[name = fname]").value;
// const lastName = document.querySelector("[name = lname]").value;


// function logformInputs(e){
//     e.preventDefault()
//     const firstName = document.querySelector("[name = fname]").value;
//     const lastName = document.querySelector("[name = lname]").value;
//     console.log(firstName,lastName);
//     if(firstName === '' || lastName === ''){
//         alert("Please fill in all fields")
//     }
//     else{
//         const ul= document.querySelector(".usersAnswer");
//         const firstLi = document.createElement("li");
//         const lastLi = document.createElement("li");
//         firstLi.innerText = firstName
//         lastLi.innerText = lastName
//         ul.append(firstLi,lastLi);
//     }
// }

// form.addEventListener("submit",logformInputs);

// /*Exercise3*/
// let allBoldItems;
// function getBoldItems() {
//   allBoldItems = document.getElementsByTagName("strong");
//   return allBoldItems;
// }

// function highlight() {
//   const allBoldItems = getBoldItems();
//   for (const item of allBoldItems) {
//     item.style.color = "blue";
//   }
// }

// function returnItemsToDefault() {
//   const allBoldItems = getBoldItems();
//   for (const bolditem of allBoldItems) {
//     bolditem.style.color = "black";
//   }
// }

// const PRGRAPH = document.querySelector('#primary')
// PRGRAPH.addEventListener('mouseover', highlight)
// PRGRAPH.addEventListener('mouseout',returnItemsToDefault)

// /*Exercise5*/

// // Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// // Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.


// const PRGRAPH = document.querySelector('#primary')

// PRGRAPH.addEventListener('mouseover',() => PRGRAPH.style.color = "blue")
// PRGRAPH.addEventListener('mouseout',() => PRGRAPH.style.fontSize = "20px")
// PRGRAPH.addEventListener('click',() => PRGRAPH.style.fontFamily = "fantasy")






 





