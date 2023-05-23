const string = "word in a given String";
const words = string.split(" ");
console.log(words)


function reversed(str){
    words = str.split('')
    words.forEach{word.split("").reverse().join("")}
    return words
}

let reversedString = reversed(str)

// words.forEach(word => {
//   word = word.split("").reverse().join("");
// });

// const reversedString = words.join(" ");

console.log(reversedString); // "siht si ta gnirts"
