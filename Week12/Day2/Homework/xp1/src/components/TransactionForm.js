import { useState, useEffect, useSelector, useDispatch } from 'react'

const TransactionForm = (props) => {
    const [transaction, setTransaction] = useState({
        accountNumber: '',
        FSC: '',
        name: '',
        amount: ''
    })


    const currentIndex = useSelector(state => state.currentIndex)
    const list = useSelector(state => state.list)

    const dispatch = useDispatch()

    const handleInputChange = (e) => {
        setTransaction({ ...transaction, [e.target.name]: e.target.value })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
    }

    return (
        <>
            <form>
                <input type="text" name='accNumber' placeholder="AccountNumber" onChange={handleInputChange} value={transaction.accountNumber}></input>
                <br></br>
                <input type="text" name='FSC' placeholder="FSC" onChange={handleInputChange} value={transaction.FSC}></input>
                <br></br>
                <input type="text" name='Holder_name' placeholder="A/C Holder Name" onChange={handleInputChange} value={transaction.name}></input>
                <br></br>
                <input type="text" name='Amount' placeholder="Amount" onChange={handleInputChange} value={transaction.amount}></input>
                <br></br>
                <input type="submit" value={currentIndex === -1 ? 'Submit' : 'error'}>Submit</input>

            </form>
        </>
    )
}



// export default class TransactionForm extends Component {
//   render(){
//     return(
//         <>
//             <form>
//                 <input type="text" placeholder="AccountNumber"></input>
//                 <br></br>
//                 <input type="text" placeholder="FSC"></input>
//                 <br></br>
//                 <input type="text" placeholder="A/C Holder Name"></input>
//                 <br></br>
//                 <input type="text" placeholder="Amount"></input>
//                 <br></br>
//                 <button type="submit">Submit</button>

//             </form>
//         </>
//     )
// }}

export default TransactionForm
