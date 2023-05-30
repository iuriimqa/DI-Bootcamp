// Daily1

// function makeAllCaps(arr) {
//     const res = new Promise((resolve, reject) => {
//         if (arr.every(item => typeof item === "string")) {
//             resolve(arr.map(item => item.toUpperCase()));
//         } else {
//             reject("Not all items in arr are of string type");
//         }
//     });

//     return res;
// }

// // makeAllCaps(["apple", "pear", "banana"])
// //   .then(result => {
// //     console.log(result);
// //   })
// //   .catch(error => {
// //     console.error(error);
// //   });


// function sortWords(arr){
//     const promise = new Promise((resolve,reject) => {
//         if (arr.length > 4){
//             resolve(arr.sort((a, b) => a.localeCompare(b, 'en')))
//         }
//         else{
//             reject("Not enought long length")
//         }
//     })
//     return promise
// }

// // sortWords(["apple", "pear", "banana", "bulka","tarelka"])
// // .then(result => {
// //     console.log(result);
// //   })
// //   .catch(error => {
// //     console.error(error);
// //   });

// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//       .catch(error => console.log(error))


// Daily2

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;
  
  const toJs = (jsonString) => {
      return new Promise((resolve, reject) => {
          let objMorse = JSON.parse(jsonString);
          if (Object.keys(objMorse).length === 0) {
              reject('this string is empty -- ERROR IN 1st FUNCTION')
          } else {
            resolve(objMorse)
          }
    })
  }
  
  const toMorse = (morseJS) =>{
      return new Promise((resolve , reject)=>{
         let userStr = prompt('enter a word')
         let arrStr = userStr.split('')
         let returnArr=[]
  
         for(let i = 0 ; i < arrStr.length ; i++){
             if(arrStr[i] in morseJS){
                 returnArr.push(morseJS[arrStr[i]])
             }else{
                 reject('One letter of the prompt doesnt exist in the object ERROR SECOND FUNCTION')
             }
         }
         resolve(returnArr)
      })//end of promise
  }
  
  const joinWords = (morseTranslation) =>{
      let str =''
      morseTranslation.forEach(element => {
          str+= `${element}`
      });
      return str;
  }
  
  toJs(morse)
  .then((value)=>toMorse(value))
  .then((response)=>joinWords(response))
  .then(morse => console.log('morse',morse))
  .catch((error)=>console.log(error +'  ***CATCHED***'))

// function toJS(str) {
//     const morseObject = JSON.parse(str);
//     const isEmpty = Object.keys(morseObject).length === 0;
//     const word = prompt("Please type a word");
//     const wordarr = word.split('');

//     const promise = new Promise((resolve, reject) => {
//         if (isEmpty) {
//             reject("The JSON object is empty");
//         } else {
//             const res = wordarr.map(key => morseObject[key])
//             resolve(res);
//         }
//     });

//     return promise;
// }

// toJS(morse)
//   .then(result => {
//     console.log(result);
//   })
//   .catch(error => {
//     console.error(error);
//   });

//   const morseObject = JSON.parse(morse);

//   function toMorse(morseObj) {
//     const words = prompt("Input word or sentence");
//     const wordArray = words.trim().split('');
    
//     const promises = [];
    
//     for (const char of wordArray) {
//       const prom = new Promise((resolve, reject) => {
//         if (!(char.toLowerCase() in morseObj)) {
//           reject("Character not in JSON object");
//         } else {
//           const resx = wordArray.map(key => morseObject[key]);
//           resolve(resx);
//         }
//       });
    
//     return prom;
//   };
// }
  
// toMorse(morseObject)
//     .then(result => {
//       console.log(result);
//     })
//     .catch(error => {
//       console.error(error);
//     });


// Fibonacci numbers
// Fn = Fn-1 + Fn-2