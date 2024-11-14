import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="navbar-brand">🍲 RecipeApp</div>
      <ul className="navbar-links">
        <li>
          <Link to="/" className={location.pathname === '/' ? 'active' : ''}>Home</Link>
        </li>
        <li>
          <Link to="/dashboard" className={location.pathname === '/dashboard' ? 'active' : ''}>Dashboard</Link>
        </li>
        <li>
          <Link to="/login" className={location.pathname === '/login' ? 'active' : ''}>Login</Link>
        </li>
        <li>
          <Link to="/register" className={location.pathname === '/register' ? 'active' : ''}>Register</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
