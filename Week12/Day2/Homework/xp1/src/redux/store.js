import { createStore } from 'redux';
import reducer from '../reducers/transactionReducer';

const store = createStore(reducer);

export default store