// export const insert_transaction = (data) => {
//     console.log(“insert”, data);
//     return {
//         type: ‘INSERT’,
//         payload: data
//     }
// }
// export const update_transaction = (data) => {
//     return {
//         type: ‘UPDATE’,
//         payload: data
//     }
// }
// export const delete_transaction = (id) => {
//     return {
//         type: ‘DELETE’,
//         payload: id
//     }
// }
// export const update_current_id = (id) => {
//     return {
//         type: ‘UPDATE-INDEX’,
//         payload: id
//     }
// }

export const INSERT = 'INSERT'
export const UPDATE = 'UPDATE'
export const DELETE = 'DELETE'
export const UPDATE_INDEX = 'UPDATE_INDEX';

export const getusers = () => {
    return (dispatch) {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(res => res.json())
            .then(data => {
                dispatch({ type: USERS, payload: data })
            })
    }
}

export const insert_trx = (trx) => {
    return {
        type: INSERT,
        payload: trx
    }
}

export const update_trx = (trx) => {
    return {
        type: UPDATE,
        payload: trx
    }
}

export const delete_trx = (indx) => {
    return {
        type: DELETE,
        payload: indx
    }
}

export const update_trx_id = (indx) => {
    return {
        type: UPDATE_INDEX,
        payload: indx
    }
}