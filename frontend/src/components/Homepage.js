// src/components/Homepage.js
import React, { useEffect, useState } from "react";
import EventCard from "./EventCard";
import "../styles/homepage.css";

const Homepage = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/events/all")
      .then((res) => res.json())
      .then((data) => setEvents(data))
      .catch((err) => console.error(err));
  }, []);

  const theaters = events.filter((e) => e.category === "Theater");
  const festivals = events.filter((e) => e.category === "Festival");
  const concerts = events.filter((e) => e.category === "Concert");

  return (
    <div className="homepage">
      <header className="homepage-header">
        <h1>Discover Events</h1>
        <p>Curated for you – May 13, 2025</p>
      </header>

      <section className="event-section">
        <h2>Theaters</h2>
        <div className="event-scroll-container">
          {theaters.map((event) => (
            <EventCard key={event.id} event={event} />
          ))}
        </div>
      </section>

      <section className="event-section">
        <h2>Festivals</h2>
        <div className="event-scroll-container">
          {festivals.map((event) => (
            <EventCard key={event.id} event={event} />
          ))}
        </div>
      </section>

      <section className="event-section">
        <h2>Concerts</h2>
        <div className="event-scroll-container">
          {concerts.map((event) => (
            <EventCard key={event.id} event={event} />
          ))}
        </div>
      </section>
    </div>
  );
};

export default Homepage;