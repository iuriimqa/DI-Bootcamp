// /*Exercise1*/
// // Analyze these pieces of code before executing them. What will be the outputs ?
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);-> ['bread',"carrot", "potato", 'chicken',"apple", "orange"]

// ------2------
// const country = "USA";
// console.log([...country]); -> ['USA']

// ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray); -> [,,]

// /*Exercise2*/
// // Using the map() method, push into a new array the firstname of the user and a welcome message. You should get an array that looks like this : 

// const users = [
//     { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
//     { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
//     { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
//     { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
//     { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
//     { firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
//     { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }
//   ];
  
//   const res = users.map(user => "Hello " + user.firstName);
//   console.log(res);

// //   2. Using the filter() method, create a new array, containing only the Full Stack Residents.

// const newArr = users.filter(user => user.role = 'Full Stack Resident');
// console.log(newArr);

// // 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of the Full Stack Residents.

// const firstNames = users.filter(user => user.role = 'Full Stack Resident').map(user => user.firstName)
// console.log(firstNames);



  

// /*Exercise3*/

// // Using this array 

// //     Use the reduce() method to combine all of these into a single string.

// const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
// const sum = epic.reduce((accumulator, currentValue) => {
//   return accumulator + " " + currentValue;
// },);

// console.log(sum);

/*Exercise4*/

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];


//    1.Using the filter() method, create a new array, containing the students that passed the course.

passed = students.filter(student => student.isPassed = true);
console.log(passed)

// 2.Bonus : Chain the filter method with a forEach method, to congratulate the students with their name and course name (ie. “Good job Jenner, you passed the course in Information Technology”, “Good Job Marco you passed the course in Robotics” ect…)

const congrat = students
  .filter(student => student.isPassed === true)
  .forEach(student => {
    console.log(`Congratulations, ${student.name}, you passed ${student.course}!`);
  });

console.log(congrat);





