const {largeNumber, getCurrentDate } = require('./main.js')
const b = 5

const x = largeNumber + b
console.log(x)

let http = require('http')

// const requestListener = function (req, res) {
    
// };

const serverone = http.createServer( (req, res) => {
    console.log("test")
    res.setHeader("Content-Type", "text/html");
    res.writeHead(200);
    res.end(`<html><body><p>My module is:</p><p>${x}</p><h1>Hi there at the frontend</h1></body></html>`);
})



const server = http.createServer( (req, res) => {
    res.setHeader("Content-Type","text/html");
    res.writeHead(201);
    res.end(`<p>The date and time are: ${getCurrentDate()}</p>`)
})

// handleResponse()

serverone.listen(5000, () => console.log('I am listening....'));
server.listen(8080, () => console.log('I am listening....'));
