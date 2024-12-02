    // frontend/src/components/UserList.js

    import React, { useEffect, useState } from 'react';

    const UserList = () => {
        const [users, setUsers] = useState([]);

        useEffect(() => {
            fetch('http://127.0.0.1:5002/api/user')
                .then(response => response.json())
                .then(data => setUsers(data))
                .catch(error => console.error('Error fetching users:', error));
        }, []);

        return (
            <div>
                <h1>User List</h1>
                <ul>
                    {users.map(user => (
                        <li key={user.user_id}>{user.name}</li>
                    ))}
                </ul>
            </div>
        );
    };

    export default UserList;
    
