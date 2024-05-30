CREATE DATABASE IF NOT EXISTS hotel_db;

USE hotel_db;

CREATE TABLE IF NOT EXISTS hotel (
	hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_name VARCHAR(255) NOT NULL,
    hotel_location VARCHAR(255) NOT NULL
);

INSERT INTO hotel (hotel_id, hotel_name, hotel_location)
VALUES
(1, 'Grand Plaza', 'USA'),
(2, 'Marina Bay Sands', 'Singapore'),
(3, 'Sakura Palace Hotel', 'Japan'),
(4, 'Mandarin Palace', 'China');
