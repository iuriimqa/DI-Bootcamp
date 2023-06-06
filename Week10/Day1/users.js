const bcrypt = require('bcrypt');

const { users } = require('./modules.js');
const url = 'https://jsonplaceholder.typicode.com/users';

users(url)
  .then(data => {n
    console.log(data);
  })
  .catch(e => {
    console.log(e);
  });


