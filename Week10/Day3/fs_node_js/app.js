const fs = require('fs');
// try{
//     const data = fs.readFileSync('info','utf-8')
//     console.log(data);
// }
// catch(e){
//     console.error('Something wrong')
// }

// fs.readFile('info','utf-8',(err,data) =>{
//     if(err){
//         console.log(err);
//     }
//     else{
//         console.log(data);
//     }
// })
// console.log("The file has been read")

const data = 'this is my hello file';

// fs.writeFile('product.json',JSON.stringify(products),'utf-8',(err)=>{
//     if(err){
//         console.log(err)
//     }
// })

fs.appendFile('hello.txt','hhhjjj')