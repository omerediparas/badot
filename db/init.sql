CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number INT UNIQUE,
    type VARCHAR(50),
    price INT,
    is_booked BOOLEAN DEFAULT FALSE
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    guest_name VARCHAR(100),
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
