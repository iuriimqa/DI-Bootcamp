const knex = require('knex');

const db = knex({
    client:'pg',
    connection: {
        host:'localhost',
        port: '1233',
        user:'postgres',
        password:'admin',
        database:'dvdrental'
    }
})

db('country')
.select('*')
// .update({city:'Jerusalem'})
.where({country:'Israel'})
.then(rows =>{
    console.log(rows);
})
.catch(err => {
    console.log(err);
})