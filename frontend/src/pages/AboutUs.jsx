import React from 'react';
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

export default AboutUs;