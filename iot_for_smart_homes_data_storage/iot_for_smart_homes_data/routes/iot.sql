CREATE DATABASE IoT_for_Smart_Home;
USE IoT_for_Smart_Home;


CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE location (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    state VARCHAR(30) NOT NULL,
    city VARCHAR(50) NOT NULL, 
    zip_code VARCHAR(20) NOT NULL
);


CREATE TABLE house (
    house_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    location_id INT NOT NULL,
    house_no INT NOT NULL,
    room_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);


CREATE TABLE device (
    device_id INT PRIMARY KEY AUTO_INCREMENT,
    house_id INT NOT NULL,
    device_name VARCHAR(50) NOT NULL,
    device_type VARCHAR(50) NOT NULL,
    device_status BOOL NOT NULL,
    FOREIGN KEY (house_id) REFERENCES House(house_id)
);


CREATE TABLE sensor (
    sensor_id INT PRIMARY KEY AUTO_INCREMENT,
    device_id INT NOT NULL,
    sensor_type VARCHAR(50) NOT NULL,
    sensor_status BOOL NOT NULL,
    FOREIGN KEY (device_id) REFERENCES Device(device_id)
);


CREATE TABLE sensorData (
    sensor_data_id INT PRIMARY KEY AUTO_INCREMENT,
    sensor_id INT NOT NULL,
    data_value INT NOT NULL,
    sensor_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    unit VARCHAR(10) NOT NULL,
    FOREIGN KEY (sensor_id) REFERENCES Sensor(sensor_id)
);


CREATE TABLE alert (
    alert_ID INT PRIMARY KEY AUTO_INCREMENT,
    alert_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    message TEXT NOT NULL,
    alert_type VARCHAR(50) NOT NULL,
    alert_status BOOL NOT NULL
);


CREATE TABLE gives (
    id INT PRIMARY KEY AUTO_INCREMENT,
    device_id INT NOT NULL,
    alert_ID INT NOT NULL,
    FOREIGN KEY (device_id) REFERENCES Device(device_id),
    FOREIGN KEY (alert_ID) REFERENCES Alert(alert_ID)
);

CREATE TABLE ownes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    device_id INT NOT NULL
);


-- Trigger for the Temperature Alert Activation
DELIMITER //
CREATE TRIGGER alert_activate
BEFORE INSERT ON SensorData
FOR EACH ROW
BEGIN
   IF NEW.data_value > 45 THEN
      INSERT INTO alert (alert_time, message, alert_type, alert_status)
      VALUES (NEW.sensor_time, 'High Temperature Detected', 'Temperature', 1);
   END IF;
END;
//
DELIMITER ;




INSERT INTO user (name, email, password_hash) 
VALUES 
('Rajesh Sharma', 'rajeshsharma@gmail.com', 'hash12345'),
('Meena', 'meena@gmail.com', 'hash23456'),
('Ankit Kumar', 'ankitkumar@gmail.com', 'hash34567'),
('Sushma ', 'sushma@gmail.com', 'hash45678'),
('Pooja ', 'pooja@gmail.com', 'hash56789');


INSERT INTO location (state, city, zip_code) 
VALUES 
('Maharashtra', 'Mumbai', '400053'),
('Karnataka', 'Bangalore', '560095'),
('Delhi', 'New Delhi', '110021'),
('West Bengal', 'Kolkata', '700019'),
('Tamil Nadu', 'Chennai', '600017');


INSERT INTO house (user_id, location_id, house_no, rooms)
VALUES 
(1, 1, 101, 2),
(2, 2, 202, 3),
(3, 3, 303, 4),
(4, 4, 404, 2),
(5, 5, 505, 3);


INSERT INTO device (house_id, device_name, device_type, device_status)
VALUES 
(1, 'Smart Thermostat', 'Temperature Control', 1),
(2, 'Smart Door Lock', 'Security', 1),
(3, 'Smart Light', 'Lighting', 0),
(4, 'Smart AC', 'Temperature Control', 1),
(5, 'Smart Refrigerator', 'Appliance', 1);


INSERT INTO sensor (device_id, sensor_type, sensor_status) 
VALUES 
(1, 'Temperature', 1),
(2, 'Motion', 1),
(3, 'Light', 0),
(4, 'Temperature', 1),
(5, 'Humidity', 1);

INSERT INTO sensorData (sensor_id, data_value, sensor_time, unit) 
VALUES 
(1, 25, '2024-10-09 10:00:00', 'C'),
(2, 1, '2024-10-09 11:00:00', 'Boolean'),
(3, 0, '2024-10-09 12:00:00', 'Boolean'),
(4, 30, '2024-10-09 13:00:00', 'C'),
(5, 60, '2024-10-09 14:00:00', '%');

INSERT INTO alert (alert_time, message, alert_type, alert_status)
VALUES 
('2024-10-09 10:30:00', 'High temperature detected', 'Temperature', 1),
('2024-10-09 11:30:00', 'Motion detected', 'Security', 1),
('2024-10-09 12:30:00', 'Light turned off', 'Lighting', 0),
('2024-10-09 13:30:00', 'High temperature detected', 'Temperature', 1),
('2024-10-09 14:30:00', 'High humidity detected', 'Appliance', 1);

INSERT INTO gives (device_id, alert_ID)
VALUES 
(2, 2),
(3, 3),
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO ownes(user_id, device_id)
VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 2),
(4, 1),
(4, 2),
(3, 1),
(2, 3),
(4, 3)



SELECT device_name, device_type, device_status 
FROM device 
WHERE house_id = 1;


SELECT name, email FROM user;

SELECT COUNT(*) AS total_houses FROM house;

SELECT h.house_no, l.city, l.zip_code 
FROM house h 
JOIN Location l ON h.location_id = l.location_id;

SELECT device_name, device_type, device_status 
FROM device;

SELECT s.sensor_type, s.sensor_status 
FROM sensor s
JOIN device d ON s.device_id = d.device_id 
WHERE d.house_id = 2;



SELECT sensor_type, sensor_status 
FROM sensor 
WHERE device_id = 1;

SELECT user_id, device_id FROM ownes WHERE device_id > 2;

SELECT COUNT(*) AS online_devices 
FROM device 
WHERE device_status = 1;

SELECT data_value, sensor_time, unit 
FROM sensorData 
WHERE sensor_id = 1 
ORDER BY sensor_time DESC 
LIMIT 1;

SELECT u.name, h.house_no, l.city, l.state 
FROM User u 
JOIN house h ON u.user_id = h.user_id 
JOIN Location l ON h.location_id = l.location_id;


SELECT alert_ID, message, alert_time 
FROM alert 
WHERE alert_time > NOW() - INTERVAL 1 DAY;


SELECT sd.data_value, sd.sensor_time, sd.unit 
FROM sensorData sd 
JOIN sensor s ON sd.sensor_id = s.sensor_id 
JOIN device d ON s.device_id = d.device_id 
WHERE d.house_id = 1;


SELECT d.device_name, a.message, a.alert_time 
FROM device d 
JOIN gives g ON d.device_id = g.device_id 
JOIN alert a ON g.alert_ID = a.alert_ID;


SELECT u.name, COUNT(d.device_id) AS total_devices
FROM user u
JOIN house h ON u.user_id = h.user_id
JOIN device d ON h.house_id = d.house_id
GROUP BY u.name;

SELECT house_no, rooms 
FROM house 
WHERE room_id > 3;


SELECT alert_ID, message, alert_time 
FROM alert 
WHERE alert_type = 'Security' AND alert_status = 1;

SELECT MAX(sd.data_value) AS max_temp, MIN(sd.data_value) AS min_temp, AVG(sd.data_value) AS avg_temp
FROM sensorData sd
JOIN sensor s ON sd.sensor_id = s.sensor_id
WHERE s.sensor_type = 'Temperature Sensor';

SELECT u.name, COUNT(h.house_id) AS total_houses
FROM user u
JOIN house h ON u.user_id = h.user_id
GROUP BY u.name
HAVING COUNT(h.house_id) > 2;


SELECT d.device_name, a.message, a.alert_time
FROM device d
JOIN gives g ON d.device_id = g.device_id
JOIN alert a ON g.alert_ID = a.alert_ID
JOIN house h ON d.house_id = h.house_id
WHERE a.alert_time > NOW() - INTERVAL 1 DAY;


SELECT s.sensor_type, AVG(sd.data_value) AS avg_value
FROM sensor s
JOIN sensorData sd ON s.sensor_id = sd.sensor_id
GROUP BY s.sensor_type;