import { delete_trx, update_trx } from "../actions/transactionActions";
import {useSelector,useDispatch} from 'react-redux'

const TransactionList = (props) =>{
    const list = useSelector(state => state.list)

    const dispatch = useDispatch()
    return(
        <div>
            <h2>TransactionList</h2>
            <table style={{border:"1px solid black" }}>
                <tbody>
                    {
                        list.map((item,i) =>{
                            <tr key={i}>
                                <td>{item.accountNumber}</td>
                                <td>{item.FSC}</td>
                                <td>{item.name}</td>
                                <td>{item.amount}</td>
                                <td><button onClick={() => dispatch(update_trx)}>Edit</button></td>
                                <td><button onClick={() => dispatch(delete_trx)}>Delete</button></td>
                            </tr>
                        }
                        )
                    }
                </tbody>
            </table>
        </div>
    )
}

export default TransactionList