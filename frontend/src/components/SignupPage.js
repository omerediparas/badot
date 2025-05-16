import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "../styles/Singin_up.css";

function Signup() {
  const [formData, setFormData] = useState({
    role: "Organizer",
    first_name: "",
    middle_name: "",
    last_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const { login } = useAuth();
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleRoleChange = (role) => setFormData({ ...formData, role });

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      return setError("Passwords do not match");
    }

    try {
      const response = await fetch("http://localhost:5000/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Signup failed");
      }

      login(data.user); // Set user in global context
      navigate("/"); // Redirect to homepage
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="auth-container">
      <form className="signup-form" onSubmit={handleSubmit}>
        <h2>Sign Up</h2>
        <div className="role-switch">
          <button
            type="button"
            className={formData.role === "Organizer" ? "active" : ""}
            onClick={() => handleRoleChange("Organizer")}
          >
            Organizer
          </button>
          <button
            type="button"
            className={formData.role === "Attendee" ? "active" : ""}
            onClick={() => handleRoleChange("Attendee")}
          >
            Attendee
          </button>
        </div>

        <input
          type="text"
          name="first_name"
          placeholder="First Name"
          required
          onChange={handleChange}
        />
        <input
          type="text"
          name="middle_name"
          placeholder="Middle Name"
          onChange={handleChange}
        />
        <input
          type="text"
          name="last_name"
          placeholder="Last Name"
          required
          onChange={handleChange}
        />
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
        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirm Password"
          required
          onChange={handleChange}
        />

        {error && <p className="error">{error}</p>}
        <button type="submit">Sign Up</button>

        <p>
          Already have an account? <a href="/login">Login</a>
        </p>
      </form>
      <div className="right-panel">
        <h1>BADOT</h1>
      </div>
    </div>
  );
}

export default Signup;
