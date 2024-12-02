import React, { useState } from 'react';
import axios from 'axios';

const UserLogin = () => {
    const [credentials, setCredentials] = useState({ email: '', password: '' });
    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCredentials({ ...credentials, [name]: value });
    };

    const loginUser = async () => {
        try {
            await axios.post('/api/user/login', credentials);
            setMessage('Login successful!');
        } catch (err) {
            setMessage('Login failed');
        }
    };

    return (
        <div>
            <h2>User Login</h2>
            <input name="email" onChange={handleChange} placeholder="email" />
            <input name="password" type="password" onChange={handleChange} placeholder="Password" />
            <button onClick={loginUser}>Login</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default UserLogin;
