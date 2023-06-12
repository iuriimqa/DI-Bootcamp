import "./Hello.css"
import React from "react"
import "./HelloClass.js"
import HelloClass from "./HelloClass"
import User from "./components/User"

const Hello = () => {
    const users = [
        {
            name:'Mary',
            email:'mary@gmail.com'
        },
        {
            name:'John',
            email:'john@gmail.com'
        },
        {
            name:'Ann',
            email:'ann@gmail.com'
        }
    ]
const returnusers = users.map(item => {
     return (
        <div className="title">
            <h4>{item.name}</h4>
            <p>{item.email}</p>
        </div>
    )
})
return(
        <>
            <h1>Hello, </h1>
            {
                returnusers
            }
            <HelloClass/>
        </>
    )
}

export default Hello