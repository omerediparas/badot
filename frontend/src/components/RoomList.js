import React from 'react';

function RoomList({ rooms }) {
  return (
    <div>
      <h2>Available Rooms</h2>
      <ul>
        {rooms.map((room) => (
          <li key={room.id}>
            Room {room.number} ({room.type}) - ${room.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RoomList;
