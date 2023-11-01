import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';  // Import Routes instead of Switch
import PatientForm from './PatientForm';
import LandingPage from './LandingPage';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/record" element={<PatientForm />} />
      </Routes>
    </Router>
  );
}

export default App;

