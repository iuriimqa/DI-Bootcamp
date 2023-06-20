
import './App.css';
import MovieDetail from './components/MovieReader';
import MovieList from './components/MovieList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <MovieDetail/>
        <MovieList/>
      </header>
    </div>
  );
}

export default App;
