
// const lat = prompt("Input lat of the city")
// const lat = '32.0852997'
// const long = prompt("Input long of the city")
// const long = '34.7818064'
const city = document.getElementById('city')
const morningtime = document.getElementById('morningtime')
const eveningtime = document.getElementById('eveningtime')
const weather = document.getElementById('weather')
const temp = document.getElementById('temp')
const info = document.getElementById('info')
// const targetcity = prompt('Type your destination')

const form = document.getElementById('form');
const cityinput = document.getElementById('cityinput');
const dateinput = document.getElementById('dateinput');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    const cityx = cityinput.value;
    const date = dateinput.value;
    fetchWeather(cityx,date)
});




// fetchcity()




async function fetchWeather(cityx,date){
    try{
        const response = await fetch(`http://api.weatherapi.com/v1/current.json?key=4fd8239d12344aceb8081603230106&q=${cityx}&dt=${date}&aqi=no`)
        // const response = await fetch('http://api.weatherapi.com/v1/current.json?key=4fd8239d12344aceb8081603230106&q=48.8588897,2.320041&aqi=no')
        const data = await response.json()
        city.innerHTML = data['location']['name']
        const latx = data['location'].lat
        const longx = data['location'].lon
        const image = document.getElementById('img');
        image.src = `https:${data['current']['condition'].icon}`
        image.alt = 'Weather'
        info.appendChild(image)
        temp.innerHTML = `Temperature is: ${data['current'].temp_c} degrees`
        const sun = await fetch(`https://api.sunrisesunset.io/json?lat=${latx}&lng=${longx}&date=${date}`)
        const sundata = await sun.json()
        morningtime.innerHTML = `Best time for photo in the morning start at: ${sundata['results'].sunrise}`
        eveningtime.innerHTML = `Best time for photo in the evening start: ${sundata['results'].golden_hour}`

    } catch (error) {
        console.error(error);
    }
}


// fetchWeather(cityx,date)