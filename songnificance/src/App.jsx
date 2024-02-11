import React from 'react';
import Home from './pages/home/Home';
import Results from './pages/results/Results';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;