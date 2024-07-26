import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// Importing Pages
import HomePage from './Pages/HomePage';
import LandingPage from './Pages/LandingPage';

import { useState,useEffect } from 'react';
const App = () => {
  const [data, setData] = useState(null);
 
  useEffect(() => {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  const sendDataToBackend = () => {
    const payload = { message: 'Hello from the frontend!' };

    fetch('/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };
//should give conflict in app.js
  return (
    <Router>
      <Routes>
        <Route path="/Landing" element={<HomePage />} />
        <Route path="/" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}

export default App;
