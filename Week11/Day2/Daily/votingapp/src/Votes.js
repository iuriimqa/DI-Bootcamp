import React, { Component } from 'react';

class Votes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      languages: [
        { name: "Php", votes: 0 },
        { name: "Python", votes: 0 },
        { name: "JavaScript", votes: 0 },
        { name: "Java", votes: 0 }
      ]
    };
  }

  render() {
    const php = this.state.languages[0];
    const python = this.state.languages[1];
    const javascript = this.state.languages[2];
    const java = this.state.languages[3];

    const phpVote = () => {
      const updatedLanguages = [...this.state.languages];
      updatedLanguages[0].votes += 1;
      this.setState({ languages: updatedLanguages });
    };

    const pythonVote = () => {
      const updatedLanguages = [...this.state.languages];
      updatedLanguages[1].votes += 1;
      this.setState({ languages: updatedLanguages });
    };

    const javascriptVote = () => {
      const updatedLanguages = [...this.state.languages];
      updatedLanguages[2].votes += 1;
      this.setState({ languages: updatedLanguages });
    };

    const javaVote = () => {
      const updatedLanguages = [...this.state.languages];
      updatedLanguages[3].votes += 1;
      this.setState({ languages: updatedLanguages });
    };

    return (
      <>
        <h1>Vote Your Language!</h1>
        <h2>{php.votes} {php.name}</h2>
        <button onClick={phpVote} id="php">Click Here</button>
        <h2>{python.votes} {python.name}</h2>
        <button onClick={pythonVote} id="python">Click Here</button>
        <h2>{javascript.votes} {javascript.name}</h2>
        <button onClick={javascriptVote} id="javascript">Click Here</button>
        <h2>{java.votes} {java.name}</h2>
        <button onClick={javaVote} id="java">Click Here</button>
      </>
    );
  }
}

export default Votes;


