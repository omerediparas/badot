// components/Header.jsx
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="flex justify-between items-center p-4 border-b shadow-sm">
      <h1 className="text-2xl font-bold text-green-900">BADOT</h1>
      <nav className="space-x-6 text-sm">
        <Link to="/contact" className="hover:underline">Contact</Link>
        <Link to="/about" className="hover:underline">About Us</Link>
        <Link to="/events" className="hover:underline">Events</Link>
        <Link to="/profile" className="hover:underline">My Profile</Link>
        <Link to="/basket" className="bg-green-800 text-white px-3 py-1 rounded">Basket (3)</Link>
      </nav>
    </header>
  );
}
