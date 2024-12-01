// src/App.js
import React from 'react';
import GetSensor from './components/GetSensor';
import AddSensorData from './components/AddSensorData';
import UserLogin from './components/UserLogin';

function App() {
    return (
        <div className="App">
            <h1>Sensor Management System</h1>
            <UserLogin />
            <GetSensor />
            <AddSensorData />
        </div>
    );
}

export default App;
