import React from "react";
import { Link } from "react-router-dom";
import "../styles/homepage.css";
import "../styles/eventcard.css";

const EventCard = ({ event }) => {
  return (
    <div className="event-card">
      <img
        src={`http://localhost:5000${event.image_url.startsWith('/') ? event.image_url : '/' + event.image_url}`}
        alt={event.name}
        className="event-image"
      />
      <div className="event-content">
        <h3>{event.name}</h3>
        <p className="event-date">{event.date}</p>
        <p className="event-venue">{event.venue}</p>
        <Link to={`/event/${event.id}`} className="event-link">View Details</Link>
      </div>
    </div>
  );
};

export default EventCard;
