// const cars = (model,type,color) => {
//     return {model,type,color}};
// cars(mustang,sport, red)

async function users(url){
    try{
        const userdata = await fetch(url);
        const userx = await userdata.json();
        return userx
    }
    catch(error){console.log(error)}
}

module.exportd = {
    users
}

