import React, { useState, useEffect } from 'react';
import App from './Pages/App';
import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";

function App1() {
  const [placeholder, setPlaceholder] = useState('Hi');

  useEffect(() => {
    fetch('/hello').then(res => res.json()).then(data => {
      setPlaceholder(data.result);
    });
  }, []);

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <a href="/App" class="btn effect04" data-sm-link-text="CLICK" target="_blank"><span>Get Predictions</span></a>
        </header>
        <Route path="/app" component= {App} />
      </div>
    </Router>
  );
}

export default App1;
