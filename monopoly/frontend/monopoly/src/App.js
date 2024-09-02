import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import React, { createContext, useContext } from 'react';
import HomePage from './Pages/TeamsHomePage';
import LandingPage from './Pages/LandingPage';
import { useState, useEffect } from 'react';

export const DataContext = createContext(null);
export const LogContext = createContext(null);

const App = () => {
  const [data, setData] = useState(null);
  const [log, setLog] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/api/data');
        const result = await response.json();
        setData(result);

        const responseLogs = await fetch('/api/logs');
        const logs = await responseLogs.json();
        setLog(logs);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();

    const intervalId = setInterval(fetchData, 10000);
    return () => clearInterval(intervalId);
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

  return (
    <DataContext.Provider value={data}>
      <LogContext.Provider value={log}>
        <Router>
          <Routes>
            <Route path="/Teams" element={<HomePage />} />
            <Route path="/Landing" element={<LandingPage />} />
          </Routes>
        </Router>
      </LogContext.Provider>
    </DataContext.Provider>
  );
};

export default App;
