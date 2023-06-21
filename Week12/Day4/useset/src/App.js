
import './App.css';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <input type="text" payload="Enter the city"></input>
      <div id="container">
        <Home />
      </div>
    </div>
  );
}

export default App;
