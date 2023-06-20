import React from 'react';
import { connect } from 'react-redux';
import { increment, decrement } from '../actions/CounterAction';

const Counter = ({ counter, increment, decrement }) => {
  return (
    <div>
      <h1>Counter: {counter}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    counter: state.counter,
  };
};

export default connect(mapStateToProps, { increment, decrement })(Counter);
