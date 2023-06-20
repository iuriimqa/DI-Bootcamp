import { connect } from "react-redux"

const MovieDetails = (props) => {

  if (props.movie !==  null) {
    return (
      <>
      <h1>Movie details</h1>
      <h2>Title {props.movie.title}</h2>
      <h2>Date {props.movie.releaseDate}</h2>
      </>
    )
  }

}

const mapStateToProps = (globalState) => {
  return {
    movie : globalState.movie_selected
  }
}


export default connect(mapStateToProps)(MovieDetails)