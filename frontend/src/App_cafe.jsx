import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App_cafe.css';
import api from './services/api';

// Import page components
import Home from './pages/Home';
import Menu from './pages/Menu';
import Reservations from './pages/Reservations';
import AboutUs from './pages/AboutUs';
import Gallery from './pages/Gallery';

// Navigation component
function Navigation() {
  return (
    <nav className="main-nav">
      <div className="nav-container">
        <Link to="/" className="logo">
          <h1>EmberTable</h1>
          <span className="tagline">Fine Dining Experience</span>
        </Link>
        <ul className="nav-links">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/menu">Menu</Link></li>
          <li><Link to="/reservations">Reservations</Link></li>
          <li><Link to="/about">About Us</Link></li>
          <li><Link to="/gallery">Gallery</Link></li>
        </ul>
      </div>
    </nav>
  );
}

// Footer component
function Footer() {
  return (
    <footer className="main-footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>Contact Us</h3>
          <p>1234 Culinary Ave, Suite 100<br />Washington, DC 20002</p>
          <p>Phone: (202) 555-4567</p>
          <p>Email: info@embertable.example</p>
        </div>
        <div className="footer-section">
          <h3>Hours</h3>
          <p>Monday - Saturday: 5:00 PM - 11:00 PM</p>
          <p>Sunday: 5:00 PM - 9:00 PM</p>
        </div>
        <div className="footer-section">
          <h3>Newsletter</h3>
          <p>Subscribe to receive updates and special offers</p>
          <NewsletterForm />
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2025 EmberTable. All rights reserved.</p>
      </div>
    </footer>
  );
}

// Newsletter form component
function NewsletterForm() {
  const [email, setEmail] = React.useState('');
  const [message, setMessage] = React.useState('');
  const [loading, setLoading] = React.useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage('');

    try {
      const { data } = await api.post('/newsletter', { email });

      if (data && (data.success || data.message)) {
        setMessage('Thank you for subscribing!');
        setEmail('');
      } else {
        setMessage(data.error || 'Subscription failed. Please try again.');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="newsletter-form" onSubmit={handleSubmit}>
      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
        disabled={loading}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Subscribing...' : 'Subscribe'}
      </button>
      {message && <p className="newsletter-message">{message}</p>}
    </form>
  );
}

// Main App component
function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/menu" element={<Menu />} />
            <Route path="/reservations" element={<Reservations />} />
            <Route path="/about" element={<AboutUs />} />
            <Route path="/gallery" element={<Gallery />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
