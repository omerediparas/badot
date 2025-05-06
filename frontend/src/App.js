import React, { useState, useEffect } from 'react';
import RoomList from './components/RoomList';
import BookingForm from './components/BookingForm';

function App() {
  const [rooms, setRooms] = useState([]);

  useEffect(() => {
    fetch('/rooms')
      .then((res) => res.json())
      .then((data) => setRooms(data));
  }, []);

  return (
    <div className="App">
      <h1>Hotel Management</h1>
      <RoomList rooms={rooms} />
      <BookingForm rooms={rooms} />
    </div>
  );
}

export default App;
