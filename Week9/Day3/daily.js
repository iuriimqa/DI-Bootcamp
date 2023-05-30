// const btn =document.getElementById('gifForm')
// btn.addEventListener('submit', function(event) {
//     event.preventDefault()});


// const myForm = document.forms[0];
// const category = document.getElementById('categoryInput').value;
// const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
// let url = `https://api.giphy.com/v1/gifs/search?q=${category}&rating=g&api_key=${apiKey}`

// myForm.addEventListener('click', (event) => {
//     event.preventDefault();
// });

    


// ;


//     fetch(url)
//       .then(response => {
//         if (!response.ok) {
//           throw new Error('Network response was not OK');
//         }
//         return response.json();
//       })
//       .then(data => {
//         console.log(data['data']);
//       })
//       .catch(error => {
//         console.error(error);
//       });
    

// const myForm = document.forms[0];
const category = prompt("Input category")
const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
let url = `https://api.giphy.com/v1/gifs/search?q=${category}&api_key=${apiKey}`;

// myForm.addEventListener('click', (event) => {
//   event.preventDefault();
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not OK');
      }
      return response.json();
    })
    .then(data => {
      console.log(data['data']);
    })
    .catch(error => {
      console.error(error);
    });
// });

