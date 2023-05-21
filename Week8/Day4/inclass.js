
function insertRow(){
    let table = document.getElementsById("sampleTable").firstElementChild;
    let row = table.firstElementChild;
    const rownum = table.children.length;
    const newRow = row.cloneNode(true)
    newRow.firstElementChild.innerText = 'Row${rownum+1} cell1';
    newRow.lastElementChild.innerText = 'Row${rownum+1} cell2';
    table.appendChild(newRow)
    
}
let id;
let pos = 0;

function move(){
    let box = document.getElementById('inner');

    id = setInterval(function(){
      if(pos >= 350){
        clearInterval(id);
      }
      pos++;
      box.style.left = pos+"px";
    },5)
}

function stop(){
  clearInterval(id);
}