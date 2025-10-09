#!/usr/bin/env python3
"""
Complete build script for Cafe Fausse frontend
Creates all pages, components, and styles
"""

import os

BASE_DIR = "/Users/mihai/cafe-fausse/frontend"

# Page components and their styles
pages = {
    # Home page CSS
    "src/pages/Home.css": """/* Home Page Styles */
.hero-section {
  position: relative;
  height: 100vh;
  background-image: url('/images/home-cafe-fausse.webp');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: white;
  max-width: 800px;
  padding: 0 20px;
}

.hero-title {
  font-size: 4rem;
  margin-bottom: 1rem;
  animation: fadeInUp 1s ease;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  animation: fadeInUp 1s ease 0.2s;
  animation-fill-mode: both;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  animation: fadeInUp 1s ease 0.4s;
  animation-fill-mode: both;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.about-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.about-image img {
  width: 100%;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-card {
  text-align: center;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.testimonial-card {
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.testimonial-text {
  font-style: italic;
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.testimonial-rating {
  color: gold;
}

.cta-section {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  text-align: center;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .about-content {
    grid-template-columns: 1fr;
  }
  
  .hero-buttons {
    flex-direction: column;
  }
}""",

    # Menu page
    "src/pages/Menu.jsx": """import React, { useState, useEffect } from 'react';
import './Menu.css';

function Menu() {
  const [menuData, setMenuData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState('all');

  useEffect(() => {
    fetchMenu();
  }, []);

  const fetchMenu = async () => {
    try {
      const response = await fetch('/api/menu');
      const data = await response.json();
      setMenuData(data);
    } catch (error) {
      console.error('Error fetching menu:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="spinner"></div>;
  }

  const categories = ['all', 'starters', 'main_courses', 'desserts', 'beverages'];

  return (
    <div className="menu-page">
      <div className="page-hero">
        <h1>Our Menu</h1>
        <p>Exquisite dishes crafted with passion</p>
      </div>

      <div className="container">
        {/* Category Filter */}
        <div className="menu-filters">
          {categories.map(cat => (
            <button
              key={cat}
              className={`filter-btn ${activeCategory === cat ? 'active' : ''}`}
              onClick={() => setActiveCategory(cat)}
            >
              {cat.replace('_', ' ').charAt(0).toUpperCase() + cat.replace('_', ' ').slice(1)}
            </button>
          ))}
        </div>

        {/* Menu Items */}
        <div className="menu-sections">
          {menuData && Object.entries(menuData).map(([category, items]) => {
            if (activeCategory !== 'all' && category !== activeCategory) return null;
            
            return (
              <div key={category} className="menu-section">
                <h2 className="menu-category-title">
                  {category.replace('_', ' ').charAt(0).toUpperCase() + category.replace('_', ' ').slice(1)}
                </h2>
                <div className="menu-items">
                  {items.map(item => (
                    <div key={item.id} className="menu-item">
                      <div className="menu-item-header">
                        <h3 className="menu-item-name">{item.name}</h3>
                        <span className="menu-item-price">${item.price.toFixed(2)}</span>
                      </div>
                      <p className="menu-item-description">{item.description}</p>
                      {item.vegetarian && <span className="vegetarian-badge">🌱 Vegetarian</span>}
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Menu;""",

    # Menu CSS
    "src/pages/Menu.css": """/* Menu Page Styles */
.menu-page {
  min-height: 100vh;
  padding-bottom: 4rem;
}

.page-hero {
  background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('/images/gallery-ribeye-steak.webp');
  background-size: cover;
  background-position: center;
  padding: 150px 0 100px;
  text-align: center;
  color: white;
}

.page-hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.menu-filters {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin: 3rem 0;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 10px 20px;
  border: 2px solid var(--primary-color);
  background: transparent;
  color: var(--primary-color);
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
}

.filter-btn:hover,
.filter-btn.active {
  background: var(--primary-color);
  color: white;
}

.menu-section {
  margin-bottom: 4rem;
}

.menu-category-title {
  text-align: center;
  font-size: 2rem;
  color: var(--primary-color);
  margin-bottom: 2rem;
  position: relative;
}

.menu-category-title::after {
  content: '';
  display: block;
  width: 100px;
  height: 3px;
  background: var(--secondary-color);
  margin: 1rem auto;
}

.menu-items {
  display: grid;
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.menu-item {
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.menu-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

.menu-item-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 0.5rem;
}

.menu-item-name {
  color: var(--primary-color);
  font-size: 1.3rem;
}

.menu-item-price {
  color: var(--secondary-color);
  font-size: 1.2rem;
  font-weight: bold;
}

.menu-item-description {
  color: #666;
  line-height: 1.6;
}

.vegetarian-badge {
  display: inline-block;
  margin-top: 0.5rem;
  padding: 5px 10px;
  background: #e8f5e9;
  color: #2e7d32;
  border-radius: 15px;
  font-size: 0.875rem;
}""",

    # Reservations page
    "src/pages/Reservations.jsx": """import React, { useState } from 'react';
import './Reservations.css';

function Reservations() {
  const [formData, setFormData] = useState({
    customer_name: '',
    email: '',
    phone_number: '',
    date: '',
    time: '',
    number_of_guests: 2,
    special_requests: '',
    newsletter_signup: false
  });

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage(null);

    // Combine date and time for time_slot
    const timeSlot = `${formData.date}T${formData.time}:00`;

    try {
      const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...formData,
          time_slot: timeSlot
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage({
          type: 'success',
          text: `Reservation confirmed! Table ${data.reservation.table_number} has been reserved for you.`
        });
        // Reset form
        setFormData({
          customer_name: '',
          email: '',
          phone_number: '',
          date: '',
          time: '',
          number_of_guests: 2,
          special_requests: '',
          newsletter_signup: false
        });
      } else {
        setMessage({
          type: 'error',
          text: data.error || 'Failed to make reservation. Please try again.'
        });
      }
    } catch (error) {
      setMessage({
        type: 'error',
        text: 'An error occurred. Please try again later.'
      });
    } finally {
      setLoading(false);
    }
  };

  // Generate time slots for restaurant hours
  const generateTimeSlots = () => {
    const slots = [];
    for (let hour = 17; hour <= 22; hour++) {
      for (let min = 0; min < 60; min += 30) {
        const time = `${hour.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}`;
        slots.push(time);
      }
    }
    return slots;
  };

  return (
    <div className="reservations-page">
      <div className="page-hero">
        <h1>Make a Reservation</h1>
        <p>Book your unforgettable dining experience</p>
      </div>

      <div className="container">
        <div className="reservation-content">
          <div className="reservation-form-section">
            <h2>Reserve Your Table</h2>
            
            {message && (
              <div className={`alert alert-${message.type}`}>
                {message.text}
              </div>
            )}

            <form onSubmit={handleSubmit} className="reservation-form">
              <div className="form-row">
                <div className="form-group">
                  <label className="form-label">Name *</label>
                  <input
                    type="text"
                    name="customer_name"
                    value={formData.customer_name}
                    onChange={handleChange}
                    className="form-input"
                    required
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Email *</label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className="form-input"
                    required
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label className="form-label">Phone</label>
                  <input
                    type="tel"
                    name="phone_number"
                    value={formData.phone_number}
                    onChange={handleChange}
                    className="form-input"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Number of Guests *</label>
                  <select
                    name="number_of_guests"
                    value={formData.number_of_guests}
                    onChange={handleChange}
                    className="form-select"
                    required
                  >
                    {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(n => (
                      <option key={n} value={n}>{n} {n === 1 ? 'Guest' : 'Guests'}</option>
                    ))}
                  </select>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label className="form-label">Date *</label>
                  <input
                    type="date"
                    name="date"
                    value={formData.date}
                    onChange={handleChange}
                    className="form-input"
                    min={new Date().toISOString().split('T')[0]}
                    required
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Time *</label>
                  <select
                    name="time"
                    value={formData.time}
                    onChange={handleChange}
                    className="form-select"
                    required
                  >
                    <option value="">Select a time</option>
                    {generateTimeSlots().map(slot => (
                      <option key={slot} value={slot}>{slot}</option>
                    ))}
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label className="form-label">Special Requests</label>
                <textarea
                  name="special_requests"
                  value={formData.special_requests}
                  onChange={handleChange}
                  className="form-textarea"
                  rows="3"
                  placeholder="Dietary restrictions, special occasions, etc."
                />
              </div>

              <div className="form-group">
                <label className="checkbox-label">
                  <input
                    type="checkbox"
                    name="newsletter_signup"
                    checked={formData.newsletter_signup}
                    onChange={handleChange}
                  />
                  <span>Subscribe to our newsletter for special offers</span>
                </label>
              </div>

              <button type="submit" className="btn btn-submit" disabled={loading}>
                {loading ? 'Processing...' : 'Reserve Table'}
              </button>
            </form>
          </div>

          <div className="reservation-info">
            <h3>Reservation Information</h3>
            <div className="info-card">
              <h4>Hours of Operation</h4>
              <p>Monday - Saturday: 5:00 PM - 11:00 PM</p>
              <p>Sunday: 5:00 PM - 9:00 PM</p>
            </div>
            
            <div className="info-card">
              <h4>Cancellation Policy</h4>
              <p>Please call us at least 24 hours in advance if you need to cancel or modify your reservation.</p>
            </div>
            
            <div className="info-card">
              <h4>Contact Us</h4>
              <p>Phone: (202) 555-4567</p>
              <p>Email: reservations@cafefausse.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Reservations;""",

    # AboutUs page
    "src/pages/AboutUs.jsx": """import React from 'react';
import './AboutUs.css';

function AboutUs() {
  return (
    <div className="about-page">
      <div className="page-hero">
        <h1>About Café Fausse</h1>
        <p>Our Story of Culinary Excellence</p>
      </div>

      <div className="container">
        <section className="about-story">
          <h2>Our Story</h2>
          <p className="lead">
            Founded in 2010 by Chef Antonio Rossi and restaurateur Maria Lopez, 
            Café Fausse blends traditional Italian flavors with modern culinary innovation.
          </p>
          <p>
            Our mission is to provide an unforgettable dining experience that reflects 
            both quality and creativity. Every dish we serve is a testament to our 
            commitment to excellence and our passion for exceptional cuisine.
          </p>
          <p>
            Located in the heart of Washington, DC, Café Fausse has become a landmark 
            destination for those seeking not just a meal, but a culinary journey that 
            engages all the senses.
          </p>
        </section>

        <section className="founders">
          <h2>Meet Our Founders</h2>
          <div className="founders-grid">
            <div className="founder-card">
              <h3>Chef Antonio Rossi</h3>
              <p className="founder-title">Executive Chef & Co-Founder</p>
              <p>
                With over 20 years of culinary experience across Europe and America, 
                Chef Rossi brings innovation and tradition to every plate. Trained at 
                Le Cordon Bleu Paris, he has worked in Michelin-starred restaurants 
                before founding Café Fausse.
              </p>
            </div>
            <div className="founder-card">
              <h3>Maria Lopez</h3>
              <p className="founder-title">Restaurateur & Co-Founder</p>
              <p>
                Maria's vision for exceptional hospitality and attention to detail has 
                shaped Café Fausse into the premier dining destination it is today. 
                Her expertise in restaurant management ensures every guest receives 
                an unforgettable experience.
              </p>
            </div>
          </div>
        </section>

        <section className="philosophy">
          <h2>Our Philosophy</h2>
          <div className="philosophy-grid">
            <div className="philosophy-item">
              <h3>🌿 Locally Sourced</h3>
              <p>We partner with local farms and suppliers to ensure the freshest ingredients.</p>
            </div>
            <div className="philosophy-item">
              <h3>🎨 Culinary Artistry</h3>
              <p>Each dish is crafted as a work of art, balancing flavor, texture, and presentation.</p>
            </div>
            <div className="philosophy-item">
              <h3>🌟 Exceptional Service</h3>
              <p>Our team is dedicated to providing warm, attentive service that exceeds expectations.</p>
            </div>
            <div className="philosophy-item">
              <h3>🍷 Perfect Pairings</h3>
              <p>Our sommelier curates wine selections that complement our cuisine perfectly.</p>
            </div>
          </div>
        </section>

        <section className="awards">
          <h2>Awards & Recognition</h2>
          <div className="awards-list">
            <div className="award-item">
              <span className="award-year">2022</span>
              <h4>Culinary Excellence Award</h4>
              <p>DC Restaurant Association</p>
            </div>
            <div className="award-item">
              <span className="award-year">2023</span>
              <h4>Restaurant of the Year</h4>
              <p>Washington Food Critics</p>
            </div>
            <div className="award-item">
              <span className="award-year">2023</span>
              <h4>Best Fine Dining Experience</h4>
              <p>Foodie Magazine</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default AboutUs;""",

    # Gallery page
    "src/pages/Gallery.jsx": """import React, { useState, useEffect } from 'react';
import './Gallery.css';

function Gallery() {
  const [galleryData, setGalleryData] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchGallery();
  }, []);

  const fetchGallery = async () => {
    try {
      const response = await fetch('/api/gallery');
      const data = await response.json();
      setGalleryData(data);
    } catch (error) {
      console.error('Error fetching gallery:', error);
    } finally {
      setLoading(false);
    }
  };

  const openLightbox = (image) => {
    setSelectedImage(image);
  };

  const closeLightbox = () => {
    setSelectedImage(null);
  };

  if (loading) {
    return <div className="spinner"></div>;
  }

  // Local images for gallery
  const localImages = [
    { id: 1, url: '/images/gallery-cafe-interior.webp', caption: 'Elegant Dining Room' },
    { id: 2, url: '/images/gallery-ribeye-steak.webp', caption: 'Signature Ribeye Steak' },
    { id: 3, url: '/images/gallery-special-event.webp', caption: 'Private Events' },
    { id: 4, url: '/images/home-cafe-fausse.webp', caption: 'Restaurant Exterior' }
  ];

  return (
    <div className="gallery-page">
      <div className="page-hero">
        <h1>Gallery</h1>
        <p>A Visual Journey Through Café Fausse</p>
      </div>

      <div className="container">
        <section className="gallery-section">
          <h2>Our Space</h2>
          <div className="gallery-grid">
            {localImages.map(image => (
              <div key={image.id} className="gallery-item" onClick={() => openLightbox(image)}>
                <img src={image.url} alt={image.caption} />
                <div className="gallery-overlay">
                  <p>{image.caption}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {galleryData && galleryData.awards && (
          <section className="awards-section">
            <h2>Awards & Recognition</h2>
            <div className="awards-grid">
              {galleryData.awards.map((award, index) => (
                <div key={index} className="award-card">
                  <div className="award-icon">🏆</div>
                  <h3>{award.title}</h3>
                  <p className="award-year">{award.year}</p>
                  <p className="award-org">{award.organization}</p>
                </div>
              ))}
            </div>
          </section>
        )}

        <section className="reviews-section">
          <h2>Guest Reviews</h2>
          <div className="reviews-grid">
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "Exceptional ambiance and unforgettable flavors. Café Fausse delivers 
                an extraordinary dining experience every time."
              </p>
              <p className="review-author">- Gourmet Review</p>
            </div>
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "A must-visit restaurant for food enthusiasts. The attention to detail 
                and quality is unmatched in the DC area."
              </p>
              <p className="review-author">- The Daily Bite</p>
            </div>
          </div>
        </section>
      </div>

      {/* Lightbox */}
      {selectedImage && (
        <div className="lightbox" onClick={closeLightbox}>
          <div className="lightbox-content">
            <img src={selectedImage.url} alt={selectedImage.caption} />
            <p>{selectedImage.caption}</p>
            <button className="lightbox-close" onClick={closeLightbox}>×</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Gallery;""",
}

# CSS files for pages
css_files = {
    "src/pages/Reservations.css": """/* Reservations Page Styles */
.reservation-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 3rem;
  max-width: 1200px;
  margin: 3rem auto;
}

.reservation-form {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.alert {
  padding: 1rem;
  border-radius: 5px;
  margin-bottom: 1rem;
}

.alert-success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.alert-error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.btn-submit {
  width: 100%;
  padding: 15px;
  font-size: 1.1rem;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  margin-bottom: 1rem;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}

@media (max-width: 768px) {
  .reservation-content {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}""",

    "src/pages/AboutUs.css": """/* About Us Page Styles */
.about-story {
  max-width: 800px;
  margin: 3rem auto;
  text-align: center;
}

.lead {
  font-size: 1.3rem;
  font-weight: 300;
  margin-bottom: 2rem;
  color: var(--primary-color);
}

.founders-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.founder-card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.founder-title {
  color: var(--secondary-color);
  font-style: italic;
  margin-bottom: 1rem;
}

.philosophy-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.philosophy-item {
  text-align: center;
  padding: 2rem;
}

.philosophy-item h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.awards-list {
  max-width: 600px;
  margin: 3rem auto;
}

.award-item {
  display: flex;
  gap: 2rem;
  align-items: center;
  padding: 1.5rem;
  background: white;
  border-radius: 10px;
  margin-bottom: 1rem;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}

.award-year {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--secondary-color);
}""",

    "src/pages/Gallery.css": """/* Gallery Page Styles */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: scale(1.05);
}

.gallery-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.gallery-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: white;
  padding: 1rem;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-overlay {
  transform: translateY(0);
}

.lightbox {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  cursor: pointer;
}

.lightbox-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.lightbox-content img {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.lightbox-content p {
  color: white;
  text-align: center;
  margin-top: 1rem;
  font-size: 1.2rem;
}

.lightbox-close {
  position: absolute;
  top: -40px;
  right: -40px;
  background: none;
  border: none;
  color: white;
  font-size: 3rem;
  cursor: pointer;
}

.awards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.award-card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.award-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.award-year {
  color: var(--secondary-color);
  font-weight: bold;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.review-card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.review-stars {
  color: gold;
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.review-text {
  font-style: italic;
  margin-bottom: 1rem;
  line-height: 1.6;
}

.review-author {
  color: var(--primary-color);
  font-weight: 600;
}"""
}

def create_file(path, content):
    """Create a file with the given content"""
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")

# Main execution
if __name__ == "__main__":
    print("Building ALL Cafe Fausse Components...")
    print("=" * 50)
    
    # Create page components
    for file_path, content in pages.items():
        create_file(file_path, content)
    
    # Create CSS files
    for file_path, content in css_files.items():
        create_file(file_path, content)
    
    print("=" * 50)
    print("All components created successfully!")
    print("\nTo start the application:")
    print("1. Backend: cd backend && source venv/bin/activate && python3 app_cafe.py")
    print("2. Frontend: cd frontend && npm run dev")
    print("3. Visit: http://localhost:5173")
