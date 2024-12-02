import React, { useState, useEffect } from 'react';

const UpdateUser = ({ userId }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    // Fetch the user's current data when the component mounts
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:5002/api/user/${userId}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setUsername(data.username);
                // Do not expose passwords for security reasons
            } catch (error) {
                setError(error.message);
            }
        };

        fetchUserData();
    }, [userId]);

    const handleUpdate = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch(`http://127.0.0.1:5002/api/user/${userId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                throw new Error('Failed to update user');
            }

            const data = await response.json();
            console.log('User updated:', data);
            setSuccessMessage('User updated successfully!');
            setError(null); // Clear any previous errors
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <form onSubmit={handleUpdate}>
            <h2>Update User</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="New Username"
                required
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="New Password"
                required
            />
            <button type="submit">Update User</button>
        </form>
    );
};

export default UpdateUser;