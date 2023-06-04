const { users } = require('./modules.js');
const url = 'https://jsonplaceholder.typicode.com/users';

users(url)
  .then(data => {
    console.log(data);
  })
  .catch(e => {
    console.log(e);
  });
