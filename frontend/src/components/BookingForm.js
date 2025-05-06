import React, { useState } from 'react';

function BookingForm({ rooms }) {
  const [guestName, setGuestName] = useState('');
  const [roomId, setRoomId] = useState('');
  const [checkIn, setCheckIn] = useState('');
  const [checkOut, setCheckOut] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/book', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ guestName, roomId, checkIn, checkOut }),
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Book a Room</h2>
      <input
        type="text"
        placeholder="Guest Name"
        value={guestName}
        onChange={(e) => setGuestName(e.target.value)}
      />
      <select onChange={(e) => setRoomId(e.target.value)} value={roomId}>
        <option value="">Select a room</option>
        {rooms.map((room) => (
          <option key={room.id} value={room.id}>
            Room {room.number}
          </option>
        ))}
      </select>
      <input
        type="date"
        placeholder="Check-In"
        value={checkIn}
        onChange={(e) => setCheckIn(e.target.value)}
      />
      <input
        type="date"
        placeholder="Check-Out"
        value={checkOut}
        onChange={(e) => setCheckOut(e.target.value)}
      />
      <button type="submit">Book</button>
    </form>
  );
}

export default BookingForm;
