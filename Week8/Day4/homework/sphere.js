
// console.log(radius)

const form = document.querySelector('form')
function getValuesForm(event){
    event.preventDefault();
    const radius = document.getElementById('radius').value
    const volume = document.getElementById('volume')
    const p = 3.14
    let res = radius*radius*p
    volume.value = res
    
}
form.addEventListener('submit',getValuesForm)

