// /*Exercise1*/
// function displayNumbersDivisible(divisor){
//     res = 0
//     for(i = 0;i<500;i++){
//         if (i%divisor == 0){
//             console.log(i)
//             res += i

//         }
//     } 
//     console.log(res)
// }
// displayNumbersDivisible(45)

// /*Exercise2*/

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// } 

// let shoppingList = ["banana", "orange", "apple"];

// function myBill() {
//     let price = 0;
//     for (let i in shoppingList) {
//         if (shoppingList[i] in stock && stock[shoppingList[i]]>0) {
//             price += prices[shoppingList[i]];
//             stock[shoppingList[i]]= stock[shoppingList[i]]-1;
//         }
//     }
//     console.log(price);
//     console.log(stock);
// }

// myBill()

// /*Exercise3*/
// function changeEnough(itemPrice, [quarters,dimes,nickel,penny]){
//     let change = (quarters*0.25)+(dimes*0.10)+(nickel*0.05)+(penny*0.01)
//     console.log(change)
//     if(change >= itemPrice){
//         console.log("Change is enought")
//     }
//     else{
//         console.log("Sorry Buddy")
//     }

// }
// changeEnough(9.25, [25, 20, 5, 0])

// /*Exercise4*/
// function hotelCost(){
// let userInput;
// while (true) {
//   userInput = prompt("Please write a number of days");

//   if (!isNaN(userInput)) {
//     break;
//   }
// }
// let cost = 142*userInput
// console.log(`Hotel price is ${cost} $`)
// return cost
// }

// // hotelCost()

// function planeRideCost(){
//     let userInput;
// while (true) {
//   userInput = prompt("Please write a country of destination");

//   const validDestinations = ['London', 'Paris', 'Berlin', 'Rome'];

//   if (validDestinations.includes(userInput)) {
//     break;
//   }
// }
// let planecost = 0
// if (userInput === 'London') {
//     planecost = 183;
//   } else if (userInput === 'Paris') {
//     planecost = 220;
// }
// else{planecost = 300}
    
// console.log(`Plane price is ${planecost} $`)
// return planecost
// }

// // planeRideCost()

// function rentalCarCost(){
//     let userInput;
//     while (true) {
//       userInput = prompt("Please write a number of days");
    
//       if (!isNaN(userInput)) {
//         break;
//       }
//     }
//     let carcost = 0
//     if(userInput>10){
//         carcost += ((userInput*40)*0.95)
//     }
//     else{
//         carcost += (userInput*40)
//     }
//     console.log(`Car cost is ${carcost} $`)
//     return carcost
// }

// // rentalCarCost()

// function totalVacationCost(){
//     let cost = hotelCost();
//     let planecost = planeRideCost();
//     let carcost = rentalCarCost();
//     let total = cost + planecost + carcost;
//     console.log(total);
//   }
  
//   totalVacationCost();