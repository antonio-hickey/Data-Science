import React, { useState, useEffect } from 'react';
import logo from '../logo.svg';
import '../App.css';


function App() {
  const [placeholder, setPlaceholder] = useState('Hi');

  useEffect(() => {
    fetch('/hello').then(res => res.json()).then(data => {
      setPlaceholder(data.result);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a href="/App" class="btn effect04" data-sm-link-text="CLICK" target="_blank"><span>Get Predictions</span></a>
      </header>
    </div>
  );
}

export default App;
