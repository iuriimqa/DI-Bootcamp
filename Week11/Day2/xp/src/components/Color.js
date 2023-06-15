import React, { Component } from 'react';

class Color extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: 'red'
    };
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ favoriteColor: 'yellow' });
    }, 5000);
  }

  render() {
    return (
      <h1>My Favorite color is {this.state.favoriteColor}</h1>
    );
  }
}

export default Color