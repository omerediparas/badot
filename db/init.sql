
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

INSERT INTO events (name, category, date, venue, price, image_url)
VALUES
  ('Rock Concert', 'Concert', '2025-05-20 20:00:00', 'City Arena', 50.00, '/images/concert1.jpg'),
  ('Theater Play', 'Theater', '2025-06-15 19:00:00', 'Downtown Theater', 35.00, '/images/play1.jpg');