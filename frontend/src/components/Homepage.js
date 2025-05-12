import React, { useEffect, useState, useRef } from "react";
import { Link } from "react-router-dom";
import { ChevronLeft, ChevronRight } from "lucide-react";


const SectionCarousel = ({ title, events }) => {
  const scrollRef = useRef();

  const scroll = (direction) => {
    if (scrollRef.current) {
      scrollRef.current.scrollBy({
        left: direction === "left" ? -300 : 300,
        behavior: "smooth",
      });
    }
  };

  return (
    <section className="mb-16">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-3xl font-bold">{title}</h2>
        <div className="flex gap-2">
          <button onClick={() => scroll("left")} className="hover:text-blue-500">
            <ChevronLeft size={24} />
          </button>
          <button onClick={() => scroll("right")} className="hover:text-blue-500">
            <ChevronRight size={24} />
          </button>
        </div>
      </div>
      <div
        ref={scrollRef}
        className="flex overflow-x-auto gap-6 scrollbar-hide scroll-smooth"
      >
        {events.map((event) => (
          <div
            key={event.id}
            className="min-w-[240px] max-w-[240px] flex-shrink-0 bg-white rounded-2xl shadow-md border border-gray-100 hover:shadow-xl transition-all"
          >
            <img
              src={event.image}
              alt={event.title}
              className="rounded-t-2xl h-40 w-full object-cover"
            />
            <div className="p-4">
              <h3 className="font-semibold text-lg">{event.title}</h3>
              <p className="text-sm text-gray-500">{event.date}</p>
              <p className="text-xs text-gray-400">{event.location}</p>
              <Link
                to={`/event/${event.id}`}
                className="block mt-3 text-center bg-blue-600 text-white text-sm py-1 rounded-xl hover:bg-blue-700"
              >
                View
              </Link>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

const Homepage = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
  fetch("http://localhost:5000/api/events")
    .then(res => res.json())
    .then(data => setEvents(data))
    .catch(err => console.error(err));
}, []);

  const theaters = events.filter((e) => e.category === "Theater");
  const festivals = events.filter((e) => e.category === "Festival");
  const concerts = events.filter((e) => e.category === "Concert");

  return (
    <div className="px-8 py-6">
      <header className="text-center mb-12">
        <h1 className="text-5xl font-serif font-bold mb-2">Events</h1>
        <p className="text-sm text-gray-500">Fresh — March 22, 2025</p>
      </header>

      {/* Optional Filters */}
      <div className="flex justify-end items-center mb-6 gap-4 text-sm">
        <span className="text-gray-600">Filter by</span>
        <select className="border rounded px-2 py-1">
          <option>Default</option>
          <option>Price</option>
          <option>Date</option>
        </select>
        <button className="border px-3 py-1 rounded">More Filters</button>
      </div>

      <SectionCarousel title="Theaters" events={theaters} />
      <SectionCarousel title="Festivals" events={festivals} />
      <SectionCarousel title="Concerts" events={concerts} />
    </div>
  );
};

export default Homepage;
