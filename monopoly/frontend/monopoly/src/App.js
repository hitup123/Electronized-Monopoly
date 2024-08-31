import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// Importing Pages
import React, { createContext, useContext } from 'react';
import HomePage from './Pages/TeamsHomePage';
import LandingPage from './Pages/LandingPage';

import { useState,useEffect } from 'react';
// const App = () => {
//   const [data, setData] = useState(null);
 
//    useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const response = await fetch('/api/data');
//         const result = await response.json();
//         setData(result);
//       } catch (error) {
//         console.error('Error fetching data:', error);
//       }
//     };

//     // Fetch data immediately
//     fetchData();

//     // Fetch data every 1 second
//     const intervalId = setInterval(fetchData, 10000);

//     // Clean up interval on component unmount
//     return () => clearInterval(intervalId);
//   }, []);

//   const sendDataToBackend = () => {
//     const payload = { message: 'Hello from the frontend!' };

//     fetch('/api/submit', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(payload)
//     })
//       .then(response => response.json())
//       .then(data => console.log(data))
//       .catch(error => console.error(error));
//   };

// //should give conflict in app.js
//   return (
//     <Router>
//       <Routes>
//         <Route path="/Teams" element={<HomePage />} jspck={data} />
//         <Route path="/Landing" element={<LandingPage />} />
//       </Routes>
//     </Router>
//   );
// }
export const DataContext = createContext(null);

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/api/data');
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    // Fetch data immediately
    fetchData();

    // Fetch data every 1 second
    const intervalId = setInterval(fetchData, 10000);

    // Clean up interval on component unmount
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
      <Router>
        <Routes>
          <Route path="/Teams" element={<HomePage />} />
          <Route path="/Landing" element={<LandingPage />} />
        </Routes>
      </Router>
    </DataContext.Provider>
  );
};

export default App;
