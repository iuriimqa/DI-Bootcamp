import { INSERT, UPDATE, DELETE, UPDATE_INDEX } from "../actions/transactionActions";
import { addLocalStorage, getFromLocalStorage } from "../utils/storage";

const initState = {
    list: [],
    currentIndex: -1
}

const reducer = (state = initState, action = {}) => {
    switch (action.type) {
        case INSERT:
            state.list.push(action.payload)
            return { ...state, list: [...state.list], currentIndex: -1 }

        case UPDATE:
            state.list[state.currentIndex] = action.payload
            return { ...state, list:[...state.list], currentIndex: -1 }

        case DELETE:
            state.list.splice(action.payload, 1)
            return { ...state, list:[...state.list] }

        case UPDATE_INDEX:
            return { ...state }

    }
}

export default reducer