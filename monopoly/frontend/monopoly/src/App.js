
import './App.css';
import React, { useEffect, useState } from 'react';
import './App.css';


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
    <div>
      <h1>Monopoly</h1>
      <p>{data ? 'Yes' : 'noooo'}</p>
      {data && Object.entries(data).map(([key, value]) => (
        <p key={key}>{`${key}: ${value}`}</p>
      ))}
      <button onClick={sendDataToBackend}>Send Data to Backend</button>
    </div>
  );
}

export default App;
