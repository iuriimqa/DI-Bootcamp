// Exercise1

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

// Exercise2


// const myPromise = new Promise((resolve,reject) => {
//   setTimeout(() => {
//     resolve("success");
//   }, 4000);
//   setTimeout(() => {
//     reject("Some errors");
//   },2000)
// });


// myPromise.then((result) => {
//   console.log("Success");
// });

// myPromise.catch((err)=> {
//     console.log("Oops something wrong")
// })

// const PromiseS = Promise.resolve(
//     setTimeout(() => {
//         console.log("success");
//     },4000)
// )

// // Exercise3

// const Promise1 = Promise.resolve(3);
// Promise1.then(result => console.log(result));

// const Promise2 = Promise.reject("Boo");
// Promise2.then(result => console.log(result));

// Exercise4

// Quiz

