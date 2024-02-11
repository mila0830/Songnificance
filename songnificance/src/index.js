import React from 'react';

import ReactDOM from 'react-dom/client';

// import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App'; // Corrected import statement

// const code = new URLSearchParams(window.location.search).get('code');
const root = document.getElementById('root');
const rootContainer = ReactDOM.createRoot(root);

rootContainer.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  
);