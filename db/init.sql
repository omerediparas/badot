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
    image_url VARCHAR(255),
);

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    user_id INT,
    seat_number VARCHAR(10),
    guest_name VARCHAR(128),
    qr_code_path VARCHAR(128),
    FOREIGN KEY (event_id) REFERENCES events(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


INSERT INTO events (name, category, date, venue, price, image_url)
VALUES
  ('Rock Concert', 'Concert', '2025-05-20 20:00:00', 'City Arena', 50.00, '/images/concert1.jpg'),
  ('Theater Play', 'Theater', '2025-06-15 19:00:00', 'Downtown Theater', 35.00, '/images/play1.jpg'),
  ('Food Festival', 'Festival', '2025-07-10 12:00:00', 'Central Park', 20.00, '/images/festival1.jpg'),
  ('Jazz Night', 'Concert', '2025-08-05 21:00:00', 'Riverside Club', 45.00, '/images/concert2.jpg'),
  ('Art Expo', 'Festival', '2025-09-12 10:00:00', 'Gallery Hall', 25.00, '/images/festival2.jpg'),
  ('Shakespeare Drama', 'Theater', '2025-10-01 18:00:00', 'City Stage', 40.00, '/images/play2.jpg'),
  ('EDM Bash', 'Concert', '2025-11-22 22:00:00', 'Open Grounds', 60.00, '/images/concert3.jpg');
