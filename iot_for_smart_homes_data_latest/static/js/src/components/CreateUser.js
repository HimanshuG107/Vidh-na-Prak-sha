    // frontend/src/components/CreateUser.js

    import React, { useState } from 'react';

    const CreateUser = () => {
        const [username, setUsername] = useState('');
        const [password, setPassword] = useState('');

        const handleSubmit = (e) => {
            e.preventDefault();

            fetch('http://127.0.0.1:5003/api/user/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, email, password_hash })
            })
            .then(response => response.json())
            .then(data => {
                console.log('User created:', data);
            })
            .catch(error => console.error('Error creating user:', error));
        };

        return (
            <form onSubmit={handleSubmit}>
                <h2>Create User</h2>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="name"
                    required
                />
                <input
                    type="text"
                    value={email}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="email"
                    required
                />
                <input
                    type="password"
                    value={password_hash}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                <button type="submit">Create User</button>
            </form>
        );
    };

    export default CreateUser;