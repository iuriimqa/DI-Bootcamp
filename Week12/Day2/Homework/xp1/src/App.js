import TransactionForm from './components/TransactionForm';
import TransactionList from './components/TransactionList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Financial Transactions:</h1>
        <TransactionForm/>
        <TransactionList/>
      </header>
    </div>
  );
}

export default App;
