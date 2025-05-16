import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "../styles/Singin_up.css";

function Login() {
  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
    role: "Attendee" // default role selected
  });
  const [error, setError] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) =>
    setCredentials({ ...credentials, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/api/auth/signin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Login failed");
      }

      login(data.user); // Set user globally
      navigate("/"); // Redirect to homepage
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="auth-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Login</h2>
        <input
          type="email"
          name="email"
          placeholder="Email"
          required
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          required
          onChange={handleChange}
        />

        {/* Role selector */}
        <select
          name="role"
          value={credentials.role}
          onChange={handleChange}
          required
        >
          <option value="Attendee">Attendee</option>
          <option value="Organizer">Organizer</option>
          <option value="Admin">Admin</option>
        </select>

        {error && <p className="error">{error}</p>}
        <button type="submit">Login</button>

        <p>
          Don't have an account? <a href="/signup">Sign Up</a>
        </p>
      </form>
      <div className="right-panel">
        <h1>BADOT</h1>
      </div>
    </div>
  );
}

export default Login;
