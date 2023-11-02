import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';



const PatientForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    visit_instance:1,
    symptoms:'',
    diagnosis: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/patient_records', formData);
      console.log('Data submitted:', response.data);
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };
  
  return (
    <div className="patient-form">
      <h2>Record Patient Details</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
          />
        </Form.Group>

        <Form.Group controlId="age">
          <Form.Label>Age</Form.Label>
          <Form.Control
            type="number"
            name="age"
            value={formData.age}
            onChange={handleInputChange}
          />
        </Form.Group>

        <Form.Group controlId="visit_instance">
          <Form.Label>Visit No.</Form.Label>
          <Form.Control
            type="number"
            name="visit_instance"
            value={formData.visit_instance}
            onChange={handleInputChange}
          />
        </Form.Group>

        <Form.Group controlId="symptoms">
          <Form.Label>Symptoms.</Form.Label>
          <Form.Control
            as="textarea"
            name="symptoms"
            value={formData.symptoms}
            onChange={handleInputChange}
          />
        </Form.Group>

        <Form.Group controlId="diagnosis">
          <Form.Label>Diagnosis.</Form.Label>
          <Form.Control
            as="textarea"
            name="diagnosis"
            value={formData.diagnosis}
            onChange={handleInputChange}
          />
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default PatientForm;
