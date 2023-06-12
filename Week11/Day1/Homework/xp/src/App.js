import logo from './logo.svg';
import './App.css';
import React from 'react';
import {UserFavoriteColors,Exercise4} from "./User"


function App() {
  const myelementx = React.createElement('h1', {}, 'I do not use JSX!');
  const myelement = <h1>I Love JSX!</h1>;
  
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };


  
  return (
    <div className="App">
      <header className="App-header">
       {myelementx}
       {myelement}
       <h3>{user.firstName}</h3>
       <h3>{user.lastName}</h3>
       <UserFavoriteColors  userinfo = {user}/>
       <Exercise4/>
      </header>
    </div>
  );
}

export default App;
