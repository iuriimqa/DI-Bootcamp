/*Exercise1*/
function hello(){ alert("Hello world")}
setTimeout(hello,2000)

let count = 0;
function addP(){
    div = document.getElementById('container');
    p = document.createElement('p');
    p.textContent = "Hello world";
    div.append(p)
    console.log(div)
    count++
    if(count === 5){
        clearInterval(intervalId);
    }
}

// setTimeout(addP,2000)

const intervalId = setInterval(addP,2000)



const button = document.getElementById('clear')
button.addEventListener("click", () => {
    clearInterval(intervalId);
  });



