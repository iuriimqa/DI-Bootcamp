// const flip = () => {
//     const coin = Math.floor(Math.random() * 3);
//     return (coin < 2) ?
//     (coin == 0) ? 'head' : 'tail' : 'side';

// }

/*
write a function testNum that takes a number as an input and
returns a Promise that tests if the value is less than 10
value < 10 - resolve with value 'number is less than 10, success!!!'
reject with value 'number is greater or equal to 10, error!!!'
call the function and get results
*/
// XP1
// const testNum = num => {
//     let proms = new Promise((resolve, reject) => {
//         if (num < 10) {
//             resolve( num+"is less than 10, success!!!");
//         } else {
//             reject(num+"is greater or equal to 10, error!!!");
//         }
//     });

//     return proms;
// };


// testNum(9)
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err)
// })

const urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholdertypicode.com/posts",
    "https://jsonplaceholder.typicode.com/albums"
  ];

//   fetch(url)
//   .then(response => {
//     // Handle the response
//     // This function will be called when the request is completed successfully
//     // You can parse the response using response.json(), response.text(), etc.
//     return response.json(); // Return the parsed response as JSON
//   })
//   .then(data => {
//     // Handle the parsed data
//     // This function will be called with the parsed response data
//     console.log(data); // Do something with the data
//   })
//   .catch(error => {
//     // Handle errors
//     // This function will be called if there is an error during the request
//     console.error(error); // Log the error
//   });

const promises = urls.map( url => fetch(url)
.then(response => {
    response.json()
}))
console.log(promises)

Promise.all(promises)
.then(res => {
    console.log(res);
})
.catch(err => {
    console.log(err);
})
