import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// Importing Pages
import HomePage from './Pages/HomePage';
import LandingPage from './Pages/LandingPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/Landing" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}

export default App;
