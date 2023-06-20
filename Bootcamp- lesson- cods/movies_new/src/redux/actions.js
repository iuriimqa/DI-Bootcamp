
// action takes the movie selected and pass it to the reducer
export const movieChosen = (movie) => {
    return {
        type : "SELECTED_MOVIE",
        movie: movie
    }
}