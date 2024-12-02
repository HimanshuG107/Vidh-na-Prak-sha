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
            sensorDataList.style.listStyle = "decimal inside";
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
                li.textContent = `Device ID: ${device.device_id}, house ID: ${device.house_id}, device name: ${device.device_name}, device type: ${device.device_type}, device status: ${device.device_status}`
                deviceList.appendChild(li);
                console.log(li);
            });
            deviceList.style.listStyle = "decimal inside";
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
                li.textContent = `User ID: ${user.user_id}, Name: ${user.name}, Email: ${user.email}`
                userList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
}

// Function to load houses
function loadHouses() {
    fetch('/api/house/get_all_houses')
        .then(response => response.json())
        .then(data => {
            const houseList = document.getElementById('house-list');
            houseList.innerHTML = ''; // Clear previous houses
            data.forEach(house => {
                const li = document.createElement('li');
                li.textContent = `House No: ${house.house_no}, Location Id: ${house.location_id}, Room Id: ${house.room_id}, User Id: ${house.user_id}`
                houseList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching houses:', error));
}

// Function to load locations
function loadLocations() {
    fetch('/api/location/get_all_locations')
        .then(response => response.json())
        .then(data => {
            const locationList = document.getElementById('location-list');
            locationList.innerHTML = ''; // Clear previous locations
            data.forEach(location => {
                const li = document.createElement('li');
                li.textContent = `Location ID: ${location.location_id}, State: ${location.state}, City: ${location.city}, Zipcode: ${location.zipcode}`
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
    const togggleDeviceForm = document.getElementById('toggle-device-form');
    togggleDeviceForm.style.display = 'block';

});

document.getElementById('register-user').addEventListener('click', function() {
    showSection('user-section');
    loadUsers();
});

// document.getElementById('login-user').addEventListener('click', function() {
//     showSection('user-section');
// });

document.getElementById('add-house').addEventListener('click', function() {
    showSection('house-section');
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
setInterval(loadSensorData, 3000); // Update every 10 seconds

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
    const showSensorDataButton = document.getElementById('show-sensor-data');

    const sections = {
        sensors: document.getElementById('sensor-section'),
        sensor_data: document.getElementById('sensor-data-section'),
        devices: document.getElementById('device-section'),
        users: document.getElementById('user-section'),
        houses: document.getElementById('house-section'),
        locations: document.getElementById('location-section'),

    };

    const sensorSection = document.getElementById('sensor-section');
    const sensorDataSection = document.getElementById('sensor-data-section');
    const userActions = document.getElementById('user-actions');
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');
    const houseActions = document.getElementById('house-actions');
    const houseForm = document.getElementById('add-house-form');
    const togggleSensorForm = document.getElementById('toggle-sensor-form');
    const addDeviceForm = document.getElementById('add-device-form');
    const addLocationForm = document.getElementById('add-location-form');
    const sensorDataForm = document.getElementById('sensor-data-form');

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
        sensorSection.style.display = 'block';
        togggleSensorForm.style.display = 'block';
    });

    showSensorDataButton.addEventListener('click', () => {
        sensorDataSection.style.display = 'block';
        sensorDataForm.style.display = 'block';
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

    // Add House buttons
    document.getElementById('add-house').addEventListener('click', () => {
        houseForm.style.display = 'block';
    });
    // Login User
    document.getElementById('login-user').addEventListener('click', () => {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    });

    // Add House buttons
    document.getElementById('add-location').addEventListener('click', () => {
        addLocationForm.style.display = 'block';
    });

    // Add Device buttons
    document.getElementById('add-device').addEventListener('click', () => {
        addDeviceForm.style.display = 'block';
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

    // Submit action for User Login
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

    // Submit action for Add House
    document.getElementById('submit-house').addEventListener('click', () => {
        
        //CAll API here
        const apiUrl = '/api/house/add_house';
        const data = {
            user_id: document.getElementById('user_id').value,
            location_id: document.getElementById('location_id').value,
            room_id: document.getElementById('room_id').value,
            house_no: document.getElementById('house_no').value
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
                alert(`House Created Successfully`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
        addHouseForm.style.display = 'none'; // Hide form after submission
    });

    // Submit action for Add Device
    document.getElementById('submit-device').addEventListener('click', () => {
        
        //CAll API here
        const apiUrl = '/api/device/add_device';
        const data = {
            house_id: document.getElementById('house_id').value,
            device_name: document.getElementById('device_name').value,
            device_type: document.getElementById('device_type').value,
            device_status: document.getElementById('device_status').value
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
                alert(`Device Added Successfully`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
        addDeviceForm.style.display = 'none'; // Hide form after submission
    });

    // Submit action for Add Location
    document.getElementById('submit-location').addEventListener('click', () => {
        
        //CAll API here
        const apiUrl = '/api/location/add_location';
        const data = {
            state: document.getElementById('state').value,
            city: document.getElementById('city').value,
            zipcode: document.getElementById('zipcode').value
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
                alert(`Location Added Successfully`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
        addLocationForm.style.display = 'none'; // Hide form after submission
    });

    // Submit actions for Toggle Sensor 
    document.getElementById('toggle-sensor').addEventListener('click', () => {
        const sensorid = document.getElementById('sensor_id').value;

        const apiUrl = 'http://127.0.0.1:5003//api/sensor/toggle_sensor/'+sensorid;
        
        const requestOptions = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        }
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
                alert(`Sensor Toggle Successful`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
            
    });

    // Submit actions for Toggle Device 
    document.getElementById('toggle-device').addEventListener('click', () => {
        const devciceid = document.getElementById('device_id').value;

        const apiUrl = 'http://127.0.0.1:5003//api/device/toggle_device/'+devciceid;
        
        const requestOptions = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        }
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
                alert(`Device Toggle Successful`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
            
    });

    // Submit action for Sensor Data By ID
    document.getElementById('submit-show-sensor-data').addEventListener('click', () => {
        
        //CAll API here
        const apiUrl = '/api/sensor/get_sensor_data_by_id';
        const data = {
            sensor_id: document.getElementById('sensor_id').value
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
                const sensorList = document.getElementById('sensor-data-by-id-list');
                sensorList.innerHTML = ''; // Clear previous locations
                data.forEach(sensor => {
                    const li = document.createElement('li');
                    li.textContent = `Sensor ID: ${sensor.location_id}, Sensor Data: ${sensor.state}, Sensor Time: ${sensor.city}`
                    sensorList.appendChild(li);
                });
                alert(`Sensor Data Loaded Successfully`);
            })
            .catch(error => {
                console.error

            ('Error:', error);
            });
        addLocationForm.style.display = 'none'; // Hide form after submission
    });

    // Initial display
    showSection('sensors'); // Show sensor section by default
});
