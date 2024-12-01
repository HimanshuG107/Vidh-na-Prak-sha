// Function to load real-time sensor data
function loadSensorData() {
    fetch('/api/sensor/get_all_sensors') // Assuming this endpoint returns real-time data
        .then(response => response.json())
        .then(data => {
            const sensorDataList = document.getElementById('sensor-data-list');
            sensorDataList.innerHTML = ''; // Clear previous data
            data.forEach(sensor => {
                const li = document.createElement('li');
               li.textContent = `Sensor ID: ${sensor.device_id}, Sensor type: ${sensor.sensor_type}, Status: ${sensor.sensor_status}`;
                sensorDataList.appendChild(li);
                console.log(li);
            });
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

// Function to load devices
function loadDevices() {
    fetch('/api/device')
        .then(response => response.json())
        .then(data => {
            const deviceList = document.getElementById('device-list');
            deviceList.innerHTML = ''; // Clear previous devices
            data.forEach(device => {
                const li = document.createElement('li');
                li.textContent = `house ID: ${device.house_id}, device name: ${device.device_name}, device type: ${device.device_type}, device status: ${device.device_status};`
                deviceList.appendChild(li);
                console.log(li);
            });
        })
        .catch(error => console.error('Error fetching devices:', error));
}

// Function to load users
function loadUsers() {
    fetch('/api/user')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = ''; // Clear previous users
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `User ID: ${user.id}, Name: ${user.name};`
                userList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
}

// Function to load houses
function loadHouses() {
    fetch('/api/house')
        .then(response => response.json())
        .then(data => {
            const houseList = document.getElementById('house-list');
            houseList.innerHTML = ''; // Clear previous houses
            data.forEach(house => {
                const li = document.createElement('li');
                li.textContent = `House ID: ${house.id}, Address: ${house.address};`
                houseList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching houses:', error));
}

// Function to load locations
function loadLocations() {
    fetch('/api/location')
        .then(response => response.json())
        .then(data => {
            const locationList = document.getElementById('location-list');
            locationList.innerHTML = ''; // Clear previous locations
            data.forEach(location => {
                const li = document.createElement('li');
                li.textContent = `Location ID: ${location.id}, Name: ${location.name};`
                locationList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching locations:', error));
}

// Function to show a specific section
function showSection(sectionId) {
    const sections = ['sensor-section', 'device-section', 'user-section', 'house-section', 'location-section'];
    sections.forEach(section => {
        document.getElementById(section).style.display = (section === sectionId) ? 'block' : 'none';
    });
}

// Event listeners for buttons
document.getElementById('load-devices').addEventListener('click', function() {
    showSection('device-section');
    loadDevices();
});

document.getElementById('register-user').addEventListener('click', function() {
    showSection('user-section');
    loadUsers();
});

document.getElementById('load-houses').addEventListener('click', function() {
    showSection('house-section');
    loadHouses();
});

document.getElementById('load-locations').addEventListener('click', function() {
    showSection('location-section');
    loadLocations();
});

// Call loadSensorData periodically for real-time updates
setInterval(loadSensorData, 5000); // Update every 5 seconds

// Logout functionality
document.getElementById('logout').addEventListener('click', function() {
    // Implement logout logic here (e.g., clear session or token)
    alert("Logged out successfully!");
});

// Initially show the sensor section on page load
document.addEventListener('DOMContentLoaded', function() {
    showSection('sensor-section');
});
document.addEventListener('DOMContentLoaded', () => {
    const logoutButton = document.getElementById('logout');
    const showSensorsButton = document.getElementById('show-sensors');
    const showDevicesButton = document.getElementById('show-devices');
    const showUsersButton = document.getElementById('show-users');
    const showHousesButton = document.getElementById('show-houses');
    const showLocationsButton = document.getElementById('show-locations');

    const sections = {
        sensors: document.getElementById('sensor-section'),
        devices: document.getElementById('device-section'),
        users: document.getElementById('user-section'),
        houses: document.getElementById('house-section'),
        locations: document.getElementById('location-section')
    };

    const userActions = document.getElementById('user-actions');
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');

    // Logout functionality
    logoutButton.addEventListener('click', () => {
        alert("Logout successful");
    });

    // Function to show a specific section
    function showSection(section) {
        for (const key in sections) {
            sections[key].style.display = (key === section) ? 'block' : 'none';
        }
        userActions.style.display = (section === 'users') ? 'block' : 'none';
    }

    // Event listeners for navigation buttons
    showSensorsButton.addEventListener('click', () => {
        for (const key in sections) {
            sections[key].style.display = (key === section) ? 'block' : 'none';
        }
        sensors.style.display = (section === 'sensors') ? 'block' : 'none';
    });
    showDevicesButton.addEventListener('click', () => showSection('devices'));
    showUsersButton.addEventListener('click', () => {
        showSection('users');
        registerForm.style.display = 'none';
        loginForm.style.display = 'none';
    });
    showHousesButton.addEventListener('click', () => showSection('houses'));
    showLocationsButton.addEventListener('click', () => showSection('locations'));

    // User action buttons
    document.getElementById('register-user').addEventListener('click', () => {
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
    });

    document.getElementById('login-user').addEventListener('click', () => {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    });

    // Submit actions for registration 
    document.getElementById('submit-register').addEventListener('click', () => {
        const name = document.getElementById('register-name').value;
        // const email = document.getElementById('register-email').value;
        // const password = document.getElementById('register-password').value;
        //CAll API here

        const apiUrl = 'http://127.0.0.1:5003/api/user/create';
        const data = {
        name: document.getElementById('register-name').value,
        email: document.getElementById('register-email').value,
        password_hash: document.getElementById('register-password').value
        };

        const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        };

        fetch(apiUrl, requestOptions)
            .then(response => {
                if (!response.ok) {
                throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                // outputElement.textContent = JSON.stringify(data, null, 2);
                alert(`Registered User: ${name}`);
                registerForm.style.display = 'none'; // Hide form after submission
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
            
    });

    document.getElementById('submit-login').addEventListener('click', () => {
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        //CAll API here
        const apiUrl = 'http://127.0.0.1:5003//api/user/login';
        const data = {
        email: document.getElementById('login-email').value,
        password_hash: document.getElementById('login-password').value
        };

        const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        };

        fetch(apiUrl, requestOptions)
            .then(response => {
                if (!response.ok) {
                throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                // outputElement.textContent = JSON.stringify(data, null, 2);
                alert(`Login Successful for: ${email}`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
        loginForm.style.display = 'none'; // Hide form after submission
    });

    // Initial display
    showSection('sensors'); // Show sensor section by default
});
