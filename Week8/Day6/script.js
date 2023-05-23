let arr = [1,2,3,4]

function multy(arr){
    arr.forEach(item,i,arr) => {
        arr[i] = item*2
    };
    return arr
};
console.log(multy(arr))

// Exercise
// Given n, take the sum of the digits of n.
// If that value has more than one digit,
// continue reducing in this way until a single-digit
// number is produced.
// This is only applicable to the natural numbers.
// Examples
//     16  -->  1 + 6 = 7
//    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
// 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
// 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

function calc(number){
let numarr= input.split('');
numarr.reduce()

if(number.length > 1){

}}
