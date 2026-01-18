DROP DATABASE IF EXISTS hotel_db;
CREATE DATABASE hotel_db;
USE hotel_db;

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT NOT NULL UNIQUE,
    room_type VARCHAR(50),
    price DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Свободен'
);

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    hire_date DATE
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    payment_date DATE,
    amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);


INSERT INTO rooms (room_number, room_type, price, status) VALUES
(101, 'Одноместный', 3000, 'Свободен'),
(102, 'Двухместный', 5000, 'Занят'),
(103, 'Сьют', 8000, 'Свободен'),
(104, 'Двухместный', 4500, 'Свободен'),
(105, 'Сьют', 9000, 'Занят');

INSERT INTO clients (first_name, last_name, phone, email) VALUES
('Иван', 'Иванов', '+79161234567', 'ivanov@mail.com'),
('Мария', 'Петрова', '+79169876543', 'petrova@mail.com'),
('Алексей', 'Сидоров', '+79165554433', 'sidorov@mail.com'),
('Елена', 'Кузнецова', '+79167778899', 'kuznetsova@mail.com'),
('Сергей', 'Смирнов', '+79160001122', 'smirnov@mail.com');

INSERT INTO staff (first_name, last_name, position, hire_date) VALUES
('Алексей', 'Сидоров', 'Администратор', '2020-03-01'),
('Елена', 'Кузнецова', 'Уборщица', '2018-07-15'),
('Игорь', 'Волков', 'Менеджер', '2019-01-10'),
('Марина', 'Лебедева', 'Консьерж', '2021-05-20');

INSERT INTO bookings (client_id, room_id, check_in, check_out) VALUES
(1, 1, '2026-01-20', '2026-01-25'),
(2, 2, '2026-01-18', '2026-01-22'),
(3, 3, '2026-01-21', '2026-01-23'),
(4, 4, '2026-01-19', '2026-01-21'),
(5, 5, '2026-01-20', '2026-01-27');

INSERT INTO payments (booking_id, payment_date, amount, payment_method) VALUES
(1, '2026-01-19', 15000, 'Карта'),
(2, '2026-01-17', 10000, 'Наличные'),
(3, '2026-01-20', 16000, 'Карта'),
(4, '2026-01-18', 9000, 'Онлайн'),
(5, '2026-01-19', 30000, 'Карта');

SELECT * FROM rooms;

SELECT * FROM clients;

SELECT b.booking_id, c.first_name, c.last_name, r.room_number, r.room_type, b.check_in, b.check_out
FROM bookings b
JOIN clients c ON b.client_id = c.client_id
JOIN rooms r ON b.room_id = r.room_id;

SELECT p.payment_id, b.booking_id, c.first_name, c.last_name, p.amount, p.payment_method
FROM payments p
JOIN bookings b ON p.booking_id = b.booking_id
JOIN clients c ON b.client_id = c.client_id;

SELECT * FROM rooms
WHERE status='Свободен';
