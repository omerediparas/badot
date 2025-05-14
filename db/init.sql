
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) UNIQUE,
    email VARCHAR(120) UNIQUE,
    wallet_balance FLOAT DEFAULT 0.0
);

CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),        
    category VARCHAR(50),
    date DATETIME,               
    venue VARCHAR(128),           
    price DECIMAL(10, 2),
    image_url VARCHAR(255)
);

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    user_id INT,
    seat_number VARCHAR(10),
    guest_name VARCHAR(128),
    FOREIGN KEY (event_id) REFERENCES events(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO events (name, category, date, venue, price, image_url)
VALUES
  ('test event 1', 'Concert', '2025-05-20 20:00:00', 'City Arena', 50.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 2', 'Theater', '2025-06-15 19:00:00', 'Downtown Theater', 35.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 3', 'Concert', '2025-05-20 20:00:00', 'City Arena', 50.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 4', 'Theater', '2025-06-15 19:00:00', 'Downtown Theater', 35.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 5', 'Festival', '2025-05-20 20:00:00', 'City Arena', 50.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 6', 'Theater', '2025-06-15 19:00:00', 'Downtown Theater', 35.00, 'static/images/to-be-or-not-to-be-that-is-the-question.jpg');