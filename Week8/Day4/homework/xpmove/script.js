const button = document.querySelector('button');

function myMove() {
    const box = document.querySelector('#animate');
    let pos = 0;
    let id = setInterval(function() {
        if (pos == 350) {
            clearInterval(id);
        } else {
            pos++;
            box.style.left = pos + "px";
        }
    }, 1);
}

button.addEventListener('click',myMove)