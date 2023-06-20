import { connect } from "react-redux"
import { movieChosen } from "../redux/actions"

const MovieList =  (props) => {
  return (
    <>
    <h1>Movies</h1>
    <ul>
      {props.all_movies.map((item, index) => 
       <div key={index}>
          <li>{item.title}</li>
          <button onClick={ () => props.selectionMovie(item)}>Details</button>
       </div>
      )}
    </ul>
    
    
    </>
  )

}

//makes the global state available in this component
const mapStateToProps = (globalState) => {
  return {
    all_movies : globalState.movies_list
  }
}

//dispatch actions from this component
const mapDispatchToProps = (dispatch) => {
  return {
    selectionMovie : (movie) => dispatch(movieChosen(movie))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(MovieList)