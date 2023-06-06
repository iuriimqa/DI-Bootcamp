const fs = require('fs')

// fs.readFile('hello.txt','utf-8',(err,data) =>{
//         if(err){
//             console.log(err);
//         }
//         else{
//             console.log(data);
//         }
//     })
//     console.log("The file has been read")


// fs.writeFile('data.txt','utf-8',(err,data) =>{
//     if(err){
//         console.log(err);
//     }
//     else{
//         console.log(data);
//     }
// })
// console.log('File was created')

fs.appendFile('data.txt','Buy orange juice',(err,data) =>{
        if(err){
            console.log(err);
        }
        else{
            console.log(data);
        }
    })

fs.unlink('data.txt',(err,data) =>{
        console.log(data);
    })
console.log("File deleted")