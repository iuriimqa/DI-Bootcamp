import React, {Component} from 'react'


class Phone extends Component {
    constructor(props){
        super(props);
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "black",
            year: 2020
        }
    }

    changeColor= () => {
        this.setState({color:"blue"})
    }

    render(){
        return(
            <>
                <h1>My Phone is a {this.state.brand}</h1>
                <p>It is a {this.state.color} {this.state.model} from {this.state.year}</p>
                <br></br>
                <button onClick={this.changeColor}>Change color</button>
            </>
        )
    }
}

export default Phone