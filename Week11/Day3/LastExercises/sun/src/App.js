import logo from './logo.svg';
import './App.css';
import Sunrise from './Sun';
import About from "./components/About"
import Home from "./components/Home"
import Contact from "./components/Contact"
import {Routes, Route, Link} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <nav>
          {/* <Link to='/'>Home</Link>
          <Link to='/about'>About</Link>
          <Link to='/contact'>Contact</Link> */}
          <Link to='/sun'>Sunrise</Link>
      </nav>
     <Routes>
        {/* <Route path='/' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/contact'element={<Contact/>}/> */}
        <Route path='/sun'element={<Sunrise/>}/>
     </Routes>
    </div>
  );
}

export default App;
