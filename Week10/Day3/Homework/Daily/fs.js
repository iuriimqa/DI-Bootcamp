const fs = require('fs');

fs.readFile('RightLeft.txt','utf-8',(err,data)=>{
    if(err){
        console.log(err)
    }
    else{
    const string = data;
    let position = 0;
    let step =0;

    // for (let i = 0; i < string.length; i++) {
    //     const difference = string[i] === '>'? 1 : -1;
    //     position+=difference
    //     step++}
    //     console.log("Total steps: " + position);
        

    for (let i = 0; i < string.length; i++) {
    const difference = string[i] === '>'? 1 : -1;
    position+=difference
    step++
    if (position === -1){
        console.log("We hit -1, current step is:"+step)
        break;
    }
  }}})