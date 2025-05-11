import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import RoomList from './components/RoomList';
import BookingForm from './components/BookingForm';
import Homepage from './components/Homepage';

function App() {
  return (
    <Router>
      <div className="App p-4">
        <Routes>
          <Route path="/" element={<Homepage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
