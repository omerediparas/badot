import React, { useEffect, useState } from "react";
import { mockEvents } from "../services/mockEvents";
import { Link } from "react-router-dom";

const Homepage = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Simulate data fetching from mock
    setEvents(mockEvents);
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">Upcoming Events</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {events.map((event) => (
          <div
            key={event.id}
            className="rounded-2xl shadow-lg p-4 hover:shadow-xl transition border border-gray-100"
          >
            <img
              src={event.image}
              alt={event.title}
              className="rounded-xl h-48 w-full object-cover mb-4"
            />
            <h2 className="text-xl font-semibold mb-1">{event.title}</h2>
            <p className="text-gray-600 text-sm mb-2">{event.category}</p>
            <p className="text-gray-500 text-sm">
              {event.date} • {event.location}
            </p>
            <p className="text-blue-600 mt-2 font-bold">${event.price}</p>
            <Link
              to={`/event/${event.id}`}
              className="mt-4 inline-block bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700"
            >
              View Details
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Homepage;
