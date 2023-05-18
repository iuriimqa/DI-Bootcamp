// /*Exercise1*/

// const people = ["Greg", "Mary", "Devon", "James"];
// arr = people
// arr.shift()
// console.log(people)
// arr[2] = 'Jason'
// console.log(people)
// arr[arr.length]='Yuri'
// console.log(people)
// let idx = arr.indexOf('Mary')
// console.log(idx)
// arr1 = arr.slice(1,3)
// console.log(arr1)
// let idxx = people.indexOf('Foo')
// console.log(idxx)
// let last = people[people.length-1]
// console.log(last)
// for (person in people)
// {console.log(people[person])}

// for (let i = 0; i < people.length; i++) {
//     console.log(people[i]); 
  
//     if (people[i] === "Devon")
//     {break}
//   }

// /*Exercise2*/

// let colours = ['red','yellow','orange','green','blue']
// for (let i = 0; i < colours.length; i++) {
//     console.log(`My #${i+1} favorite color is: ${colours[i]}`);

// }

// const suffixes = ["st", "nd", "rd", "th", "th"];

// for (let i = 0; i < colours.length; i++) {
//     let suffix = suffixes[i];
//     if (i === 0) {
//         suffix = "st";
//     } else if (i === 1) {
//         suffix = "nd";
//     } else if (i >= 3 && i <= 20) {
//         suffix = "th";
//     } else {
//         const lastDigit = i % 10;
//         suffix = suffixes[lastDigit] || "th";
//     }
//     console.log(`My ${i + 1}${suffix} choice is ${colours[i]}`);
// }

// /*Exercise3*/
// let number = parseInt(prompt("Enter a number:"));

// while (number < 10) {
//   number = parseInt(prompt("Enter a number:"));
// }

// console.log("Number is greater than or equal to 10.");


/*Exercise4*/
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building['numberOfFloors']);
console.log(building['numberOfAptByFloor']['firstFloor']);
console.log(building['numberOfAptByFloor']['thirdFloor']);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);

let sum = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]
let dan = building.numberOfRoomsAndRent.dan[1]
console.log(sum, dan)

if (dan > sum){dan = 1200}
console.log(dan)

/*Exercise5*/
let family = {
    name:"Stiven",
    childrens:3,
    age:30
}

for (let key in family) {
    console.log(key)
    console.log(family[key])
}

/*Exercise6*/
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

  for (let key in details) {
    console.log(key,details[key])
}
/*Exercise7*/

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const arr = [];
for (let i = 0; i < names.length; i++) {
    let word = names[i];
    let firstLetter = word.charAt(0);
    arr.push(firstLetter);
  }
console.log(arr)
arr.sort();
res = arr.join('')
console.log(res)


/*Daily Stars*/
for(i = 1;i <= 6; i++){
    let stars = '';
    for (let j = 1; j <= i; j++) {
        stars += '*';
      }
      console.log(stars);
    }
/*Daily Not Word*/
 let sentense = "the movie is not so terrible bad , i like it"
 const indexNot = sentense.indexOf("not")
 const indexBad = sentense.indexOf("bad") + 3
 const replacement = "good"

 if (sentense.includes("not") && sentense.includes("bad")){
    let replaced = sentense.slice(0, indexNot) + replacement + sentense.slice(indexBad + 1);
console.log(replaced)}

