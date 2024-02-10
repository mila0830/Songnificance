import React from 'react';

import ReactDOM from 'react-dom';

// import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App'; // Corrected import statement

// const code = new URLSearchParams(window.location.search).get('code');

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);