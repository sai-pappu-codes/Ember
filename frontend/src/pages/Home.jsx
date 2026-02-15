import React from 'react';
import { Link } from 'react-router-dom';
import Newsletter from '../components/Newsletter';
import './Home.css';

function Home() {
  return (
    <div className="home-page">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-overlay"></div>
        <div className="hero-content">
          <h1 className="hero-title">Welcome to Café Fausse</h1>
          <p className="hero-subtitle">An Unforgettable Fine Dining Experience</p>
          <div className="hero-buttons">
            <Link to="/reservations" className="btn btn-primary">Make a Reservation</Link>
            <Link to="/menu" className="btn btn-secondary">View Menu</Link>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="section about-preview">
        <div className="container">
          <h2 className="section-title">Experience Excellence</h2>
          <div className="about-content">
            <div className="about-text">
              <p>
                Since 2010, Café Fausse has been the pinnacle of fine dining in Washington, DC. 
                Founded by Chef Antonio Rossi and restaurateur Maria Lopez, we blend traditional 
                Italian flavors with modern culinary innovation.
              </p>
              <p>
                Our commitment to excellence, locally sourced ingredients, and unforgettable 
                dining experiences has earned us numerous accolades and a devoted following.
              </p>
              <Link to="/about" className="btn">Learn More About Us</Link>
            </div>
            <div className="about-image">
              <img src="/images/gallery-cafe-interior.webp" alt="Cafe Fausse Interior" />
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="section features-section">
        <div className="container">
          <h2 className="section-title">Why Choose Café Fausse</h2>
          <div className="features-grid">
            <div className="feature-card" style={{backgroundImage: 'linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url(/images/dessert-closeup.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', color: 'white'}}>
              <div className="feature-icon">🍽️</div>
              <h3>Exquisite Cuisine</h3>
              <p>Masterfully crafted dishes using the finest locally sourced ingredients</p>
            </div>
            <div className="feature-card" style={{backgroundImage: 'linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url(/images/cocktail-bar.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', color: 'white'}}>
              <div className="feature-icon">🍷</div>
              <h3>Curated Wine Selection</h3>
              <p>An extensive collection of fine wines from around the world</p>
            </div>
            <div className="feature-card" style={{backgroundImage: 'linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url(/images/chef-hands.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', color: 'white'}}>
              <div className="feature-icon">👨‍🍳</div>
              <h3>Award-Winning Chef</h3>
              <p>Led by Chef Antonio Rossi, recipient of multiple culinary awards</p>
            </div>
            <div className="feature-card" style={{backgroundImage: 'linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url(/images/bar-interior.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', color: 'white'}}>
              <div className="feature-icon">🌟</div>
              <h3>Elegant Ambiance</h3>
              <p>Sophisticated atmosphere perfect for special occasions</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="section testimonials-section">
        <div className="container">
          <h2 className="section-title">What Our Guests Say</h2>
          <div className="testimonials-grid">
            <div className="testimonial-card">
              <p className="testimonial-text">
                "Exceptional ambiance and unforgettable flavors. Café Fausse delivers 
                an extraordinary dining experience every time."
              </p>
              <div className="testimonial-author">- Gourmet Review</div>
              <div className="testimonial-rating">⭐⭐⭐⭐⭐</div>
            </div>
            <div className="testimonial-card">
              <p className="testimonial-text">
                "A must-visit restaurant for food enthusiasts. The attention to detail 
                and quality is unmatched in the DC area."
              </p>
              <div className="testimonial-author">- The Daily Bite</div>
              <div className="testimonial-rating">⭐⭐⭐⭐⭐</div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section cta-section">
        <div className="container text-center">
          <h2>Ready to Experience Café Fausse?</h2>
          <p>Book your table now and prepare for an unforgettable dining experience</p>
          <Link to="/reservations" className="btn btn-large">Reserve Your Table</Link>
        </div>
      </section>

      {/* Newsletter Signup */}
      <Newsletter />

      {/* Contact Info */}
      <section className="section contact-info">
        <div className="container">
          <div className="contact-grid">
            <div className="contact-item">
              <h3>📍 Location</h3>
              <p>1234 Culinary Ave, Suite 100<br />Washington, DC 20002</p>
            </div>
            <div className="contact-item">
              <h3>📞 Phone</h3>
              <p>(202) 555-4567</p>
            </div>
            <div className="contact-item">
              <h3>🕐 Hours</h3>
              <p>Mon-Sat: 5:00 PM - 11:00 PM<br />Sunday: 5:00 PM - 9:00 PM</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
