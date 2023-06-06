const largeNumber = 356;


function getCurrentDate(){
    const now = new Date();
    console.log("now:", now);
    return now;
}

module.exports ={
    largeNumber, getCurrentDate
}