import React, { Component } from 'react';



class Garage extends Component {
    constructor(props){
        super(props);

        this.state = {
            size:'small'
        }
    }
    render() {
      return (
        <div>
          <h1>Who lives in my {this.state.size} garage?</h1>
        </div>
      );
    }
  }

export default Garage