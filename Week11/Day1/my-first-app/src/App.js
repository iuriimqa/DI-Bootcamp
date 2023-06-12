import logo from './logo.svg';
import './App.css';
// import Hello from './Hello';
import robots from "./Users.json";
import User from "./components/User.js"
import UserClass from 

console.log(robots);

function App() {
  return (
    <div>
      <header>
        {
          robots.map((item,indx) => {
            return <User userinfo={item} key={indx}/>
          })
        }
      </header>
    </div>
  );
}

export default App;
