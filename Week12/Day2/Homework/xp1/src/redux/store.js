import { applyMiddleware, createStore } from 'redux';
import reducer from '../reducers/transactionReducer';
import thunk from 'redux-thunk'


const logger = (store) = (next) => (action) => {
    console.log('prev_state=>', store.getState());
    console.log('action=>',action);
    next(action)
    console.log('curr_state=>',store.getState());
}

const store = createStore(reducer, applyMiddleware(logger,thunk));

    export default store