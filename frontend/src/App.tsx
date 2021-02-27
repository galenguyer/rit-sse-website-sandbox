import './App.css';
import Cookies from 'js-cookie';
import React from 'react';

function App() {
  return (
    <div className="App">
      <p>{Cookies.get('email')}</p>
    </div>
  );
}

export default App;
