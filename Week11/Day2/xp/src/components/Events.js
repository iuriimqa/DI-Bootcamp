import React, { Component } from 'react';

const clickMe = () => {
    alert('I was clicked')
}



const handleKeyDown = (event) => {
    if (event.key == 'Enter'){
        alert('The enter key was pressed, your input is:'  + event.target.value)
    }
}



class Events extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: 'ON'
    };
  }

  changeState = () => {if(this.state.isToggleOn == 'ON'){
    this.setState({ isToggleOn: 'OFF' });}
    else{this.setState({isToggleOn: 'ON'})}
  };

  render() {
    return (
      <div>
        <button onClick={clickMe}>Try</button>
        <br></br>
        <input onKeyDown={handleKeyDown} type='text' placeholder='Press the ENTER key!'></input>
        <br></br>
        <label>Exercise 9:</label>
        <br></br>
        <button onClick={this.changeState}>{this.state.isToggleOn}</button>
      </div>
    );
  }
}

export default Events