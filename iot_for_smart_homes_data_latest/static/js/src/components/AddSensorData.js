// src/components/AddSensorData.js
import React, { useState } from 'react';
import axios from 'axios';

const AddSensorData = () => {
    const [data, setData] = useState({}); // Adjust structure as needed
    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setData({ ...data, [name]: value });
    };

    const addSensorData = async () => {
        try {
            await axios.post('/api/sensor/add_sensorData', data);
            setMessage('Sensor data added successfully!');
        } catch (err) {
            setMessage('Error adding sensor data');
        }
    };

    return (
        <div>
            <h2>Add Sensor Data</h2>
            {/* Add form fields based on your data structure */}
            <input name="temperature" onChange={handleChange} placeholder="Temperature" />
            <input name="humidity" onChange={handleChange} placeholder="Humidity" />
            <button onClick={addSensorData}>Add Sensor Data</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default AddSensorData;
