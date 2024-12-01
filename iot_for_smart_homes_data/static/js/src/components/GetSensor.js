import React, { useState } from 'react';
import axios from 'axios';

const GetSensor = () => {
    const [sensorId, setSensorId] = useState('');
    const [sensorData, setSensorData] = useState(null);
    const [error, setError] = useState('');

    const fetchSensor = async () => {
        try {
            const response = await axios.get(`/api/sensor/get_sensor_by_sensor_id/${sensorId}`);
            setSensorData(response.data);
            setError('');
        } catch (err) {
            setError('Sensor not found');
            setSensorData(null);
        }
    };

    return (
        <div>
            <h2>Get Sensor by ID</h2>
            <input
                type="number"
                value={sensorId}
                onChange={(e) => setSensorId(e.target.value)}
                placeholder="Enter Sensor ID"
            />
            <button onClick={fetchSensor}>Fetch Sensor</button>
            {error && <p>{error}</p>}
            {sensorData && <pre>{JSON.stringify(sensorData, null, 2)}</pre>}
        </div>
    );
};

export default GetSensor;
