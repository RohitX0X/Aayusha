import React from 'react';
import { Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div >
      <h1>Welcome, Doctor!</h1>
      <Link to="/record">
        <Button variant="primary">Record</Button>
      </Link>
    </div>
  );
};

export default LandingPage;