// // Exercise 1 : Location
// // Instructions

// //     Analyze the code below. What will be the output?

// // const person = {
// //     name: 'John Doe',
// //     age: 25,
// //     location: {
// //         country: 'Canada',
// //         city: 'Vancouver',
// //         coordinates: [49.2827, -123.1207]
// //     }
// // }

// // const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// // console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`); 
// -> "I am John Doe from Vancouver, Canada.Latitude(49.2827),Longitude(-123.1207)"

// // Exercise2
// // Using the code above, destructure the parameter inside the function and return a string as the example seen below:
// // //output : 'Your full name is Elie Schoppik'


// const objUser = {first: 'Elie', last: 'Schoppik'};

// function displayStudentInfo(user) {
//     const { first, last } = user;
//     console.log(`Your full name is ${first} ${last}`);
    
// }

// displayStudentInfo(objUser);

// // Exercise3

// // Using this object const users = { user1: 18273, user2: 92833, user3: 90315 }

// //     Using methods taught in class, turn the users object into an array:
// //     Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// //     FYI : The number is their ID number.

// //     Modify the outcome of part 1, by multipling the user’s ID by 2.
// //     Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]


// const users = { user1: 18273, user2: 92833, user3: 90315 }

// function transform(a){
//     const keys = Object.keys(a);
//     const arr = keys.map(key => [key, a[key]]);
//     console.log(arr);
// }
// transform(users)


// function multyid(a){
//     const keys = Object.keys(a);
//     const multy= keys.map(key => [key, (a[key]*2)])
//     console.log(multy);
// }
// multyid(users)

// /*Exercise4*/

// // Analyze the code below. What will be the output?

// // class Person {
// //   constructor(name) {
// //     this.name = name;
// //   }
// // }

// // const member = new Person('John');
// // console.log(typeof member);
// -> object

// // Exercise5
// // Using the Dog class below:

// // class Dog {
// //   constructor(name) {
// //     this.name = name;
// //   }
// // };

// //     Analyze the options below. Which constructor will successfully extend the Dog class?
// -> 2.class Labrador extends Dog {
//     constructor(name, size) {
//       super(name);
//       this.size = size;
//     }
//   };

// Exercise6

// Evaluate these (ie True or False)

// [2] === [2] 
// {} === {}
// -> both False

// const object1 = { number: 5 }; 
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number)-> 4
// console.log(object3.number)-> 4
// console.log(object4.number)-> 5

class Animal {
    constructor(name, type, color){
        this.name = name
        this.type = type
        this.color = color
    }}

class Mammal extends Animal{
    constructor(name,color){
        super(name,"mammal",color);
    }  
    sound(arr){
        return `This animal is ${this.name}.It's name is ${this.name}, its color is ${this.color} and the sound it makes is ${arr}`;

    }
}



const Cow = new Animal("Cow","mammal","black and white");
console.log(Cow)
const Dog = new Mammal("Choowee","brown")
console.log(Dog)
console.log(Dog.sound())