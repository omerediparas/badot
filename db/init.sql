
-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS Follow;
DROP TABLE IF EXISTS Report;
DROP TABLE IF EXISTS Has;
DROP TABLE IF EXISTS Sponsorship;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Favorite;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Panel_Admin;
DROP TABLE IF EXISTS Event_Organiser;
DROP TABLE IF EXISTS Event_Attendee;
DROP TABLE IF EXISTS User_Phone;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Venue;
DROP TABLE IF EXISTS User;

-- User Table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    login_date DATE,
    nationality VARCHAR(50)
);

-- User_Phone Table
CREATE TABLE User_Phone (
    user_id INT,
    phone_number VARCHAR(20),
    PRIMARY KEY (user_id, phone_number),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Event_Attendee Table
CREATE TABLE Event_Attendee (
    user_id INT PRIMARY KEY,
    street_no INT,
    street_name VARCHAR(100),
    apartment VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    zip VARCHAR(10),
    date_of_birth DATE,
    age INT,
    budget DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Event_Organiser Table
CREATE TABLE Event_Organiser (
    user_id INT PRIMARY KEY,
    o_revenue DECIMAL(10, 2),
    rating FLOAT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Panel_Admin Table
CREATE TABLE Panel_Admin (
    user_id INT PRIMARY KEY,
    a_revenue DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Venue Table
CREATE TABLE Venue (
    venue_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100),
    street_no INT,
    street_name VARCHAR(100),
    apartment VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    zip VARCHAR(10),
    name VARCHAR(100),
    num_of_columns INT,
    num_of_rows INT,
    capacity INT,
    type ENUM('Indoor', 'Outdoor', 'Hybrid')
);

-- Event Table
CREATE TABLE Event (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    type ENUM('Concert', 'Theatre', 'Sports', 'Conference', 'Other'),
    date DATETIME,
    description TEXT,
    active_status BOOLEAN,
    rating FLOAT,
    user_id INT,
    venue_id INT,
    rules TEXT,
    image_url TEXT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (venue_id) REFERENCES Venue(venue_id)
);

-- Favorite Table
CREATE TABLE Favorite (
    user_id INT,
    event_id INT,
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES Event_Attendee(user_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id)
);

-- Feedback Table
CREATE TABLE Feedback (
    user_id INT,
    event_id INT,
    rate INT CHECK (rate >= 1 AND rate <= 5),
    comment TEXT,
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES Event_Attendee(user_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id)
);

-- Payment Table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2),
    date DATETIME,
    method ENUM('CreditCard', 'PayPal', 'Crypto', 'BankTransfer'),
    status ENUM('Pending', 'Completed', 'Failed'),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Ticket Table
CREATE TABLE Ticket (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    column_num INT,
    row_num INT,
    seat_number INT,
    seating_category ENUM('VIP', 'Regular', 'Economy'),
    price DECIMAL(10, 2),
    status ENUM('Available', 'Booked', 'Cancelled'),
    QR_code TEXT,
    payment_id INT,
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (payment_id) REFERENCES Payment(payment_id)
);

-- Book Table
CREATE TABLE Book (
    user_id INT,
    ticket_id INT,
    event_id INT,
    PRIMARY KEY (user_id, ticket_id, event_id),
    FOREIGN KEY (user_id) REFERENCES Event_Attendee(user_id),
    FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id)
);

-- Sponsorship Table
CREATE TABLE Sponsorship (
    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    sponsorship_price DECIMAL(10, 2),
    description TEXT,
    url TEXT,
    image TEXT
);

-- Has Table
CREATE TABLE Has (
    event_id INT,
    sponsor_id INT,
    PRIMARY KEY (event_id, sponsor_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (sponsor_id) REFERENCES Sponsorship(sponsor_id)
);

-- Report Table
CREATE TABLE Report (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    type ENUM('Financial', 'User', 'Technical', 'Other'),
    description TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Panel_Admin(user_id)
);

-- Follow Table
CREATE TABLE Follow (
    event_attendee_id INT,
    event_organizer_id INT,
    PRIMARY KEY (event_attendee_id, event_organizer_id),
    FOREIGN KEY (event_attendee_id) REFERENCES Event_Attendee(user_id),
    FOREIGN KEY (event_organizer_id) REFERENCES Event_Organiser(user_id)
);


INSERT INTO Event (
  name, type, date, description, active_status, rating,
  user_id, venue_id, rules, image_url
)
VALUES
  ('test event 1', 'Concert', '2025-05-20 20:00:00', 'Test event description', TRUE, 4.5, 1, 1, 'No outside food allowed.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 2', 'Theatre', '2025-06-15 19:00:00', 'Test event description', TRUE, 4.0, 2, 2, 'Arrive 15 minutes early.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 3', 'Concert', '2025-05-20 20:00:00', 'Test event description', TRUE, 4.3, 1, 1, 'ID required at entrance.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 4', 'Theatre', '2025-06-15 19:00:00', 'Test event description', TRUE, 4.2, 2, 2, 'No flash photography.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 5', 'Other', '2025-05-20 20:00:00', 'Test event description', TRUE, 3.9, 1, 1, 'Follow COVID guidelines.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg'),
  ('test event 6', 'Theatre', '2025-06-15 19:00:00', 'Test event description', TRUE, 4.1, 2, 2, 'Keep mobile phones silent.', 'static/images/to-be-or-not-to-be-that-is-the-question.jpg');