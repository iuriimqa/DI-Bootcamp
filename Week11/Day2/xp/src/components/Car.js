import React, { Component } from 'react';
import carinfo  from "../App";
import Garage from './Garage';


class Car extends Component {
    constructor(props){
        super(props);

        this.state = {
            color:'blue'
        }
    }
    render() {
      return (
        <div>
          <Garage/>
          <h1>The model is {this.state.color} {this.props.info.model}</h1>
        </div>
      );
    }
  }

export default Car