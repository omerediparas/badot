import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Header() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="flex justify-between items-center p-4 border-b shadow-sm">
      <Link to="/">
        <h1 className="text-2xl font-bold text-green-900">BADOT</h1>
      </Link>

      <nav className="space-x-6 text-sm">
        {user ? (
          <>
            <Link to="/events" className="hover:underline">Events</Link>
            <Link to="/profile" className="hover:underline">My Profile</Link>
            <Link to="/basket" className="bg-green-800 text-white px-3 py-1 rounded">Basket</Link>
            <button onClick={handleLogout} className="text-red-600 hover:underline">Logout</button>
          </>
        ) : (
          <>
            <Link to="/login" className="text-green-900 hover:underline">Sign In</Link>
            <Link to="/signup" className="bg-green-800 text-white px-3 py-1 rounded">Sign Up</Link>
          </>
        )}
      </nav>
    </header>
  );
}
