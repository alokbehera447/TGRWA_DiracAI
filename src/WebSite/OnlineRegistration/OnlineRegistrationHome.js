import React, { useState } from 'react';
import axios from 'axios';

const YourComponent = () => {
  const [formData, setFormData] = useState({
    name: '',
    mobileno: '',
    email: '',
    address: '',
    photoFile: null,
  });

  const handleInputChange = (e) => {
    const { name, value, type, files } = e.target;

    // If the input is a file input, set photoFile to the selected file
    const newValue = type === 'file' ? files[0] : value;

    setFormData({
      ...formData,
      [name]: newValue,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Create FormData to send files
      const formDataToSend = new FormData();
      formDataToSend.append('name', formData.name);
      formDataToSend.append('mobileno', formData.mobileno);
      formDataToSend.append('email', formData.email);
      formDataToSend.append('address', formData.address);
      formDataToSend.append('photoFile', formData.photoFile);

      // Make a POST request using Axios
      const response = await axios.post('http://127.0.0.1:8000/api/onlineregistration/create/', formDataToSend);

      // Handle the response as needed
      console.log(response.data);
    } catch (error) {
      // Handle errors
      console.error('Error:', error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" name="name" value={formData.name} onChange={handleInputChange} />
      </label>

      <label>
        Mobile No:
        <input type="text" name="mobileno" value={formData.mobileno} onChange={handleInputChange} />
      </label>

      <label>
        Email:
        <input type="text" name="email" value={formData.email} onChange={handleInputChange} />
      </label>

      <label>
        Address:
        <input type="text" name="address" value={formData.address} onChange={handleInputChange} />
      </label>

      <label>
        Photo:
        <input type="file" name="photoFile" onChange={handleInputChange} />
      </label>

      <button type="submit">Submit</button>
    </form>
  );
};

export default YourComponent;

