import React, { useState } from 'react';
import axios from 'axios';

const AnalyticsPage = () => {
    const [searchKeyword, setSearchKeyword] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [searchNamePhone, setSearchNamePhone] = useState('');

  const handleSearch = () => {
    // Use Axios to send a GET request to the backend
    const combinedKeyword = `${searchKeyword} ${searchNamePhone}`.trim();

    axios.get(`http://127.0.0.1:5000/api/patient_search?keyword=${combinedKeyword}`)
      .then((response) => {
        setSearchResults(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  };

  return (
    <div>
      <h2>Analytics</h2>
      <input
        type="text"
        placeholder="Enter keywords"
        value={searchKeyword}
        onChange={(e) => setSearchKeyword(e.target.value)}
      />
      <input
        type="text"
        placeholder="Search by Name/Phone"
        value={searchNamePhone}
        onChange={(e) => setSearchNamePhone(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      {/* Display search results */}
      <div>
        <h3>Search Results:</h3>
        <ul>
          {searchResults.map((patient) => (
            <li key={patient.name}>
              {patient.name} - {patient.diagnosis} - {patient.symptoms} - {patient.age} - {patient.phone}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AnalyticsPage;
