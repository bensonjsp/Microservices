CREATE DATABASE IF NOT EXISTS room_db;

USE room_db;

CREATE TABLE IF NOT EXISTS room (
	room_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    hotel_name VARCHAR(255) NOT NULL,
    room_number INT NOT NULL,
    room_size INT NOT NULL,
    room_vacancy VARCHAR(20) NOT NULL
);

INSERT INTO room (room_id, hotel_id, hotel_name, room_number, room_size, room_vacancy)
VALUES
(11, 1, 'Grand Plaza', 1011, 2, 'VACANT'),
(12, 1, 'Grand Plaza', 1012, 4, 'VACANT'),
(1000, 2, 'Marina Bay Sands', 1000, 4, 'OCCUPIED'),
(1001, 2, 'Marina Bay Sands', 1001, 4, 'VACANT'),
(3001, 3, 'Sakura Palace Hotel', 3001, 4, 'OCCUPIED'),
(3011, 3, 'Sakura Palace Hotel', 3011, 2, 'VACANT'),
(5002, 4, 'Mandarin Palace', 5002, 2, 'VACANT'),
(5008, 4, 'Mandarin Palace', 5008, 2, 'VACANT');
