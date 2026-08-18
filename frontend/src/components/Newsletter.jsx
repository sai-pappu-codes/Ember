import React, { useState } from 'react';
import './Newsletter.css';
import api from '../services/api';

function Newsletter() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!email) {
      setMessage('Please enter your email address');
      return;
    }

    setIsLoading(true);
    setMessage('');

    try {
      const { data } = await api.post('/newsletter', { email });

      if (data && (data.success || data.message)) {
        setMessage('Thank you for subscribing to our newsletter!');
        setEmail('');
      } else {
        setMessage(data.error || 'Failed to subscribe. Please try again.');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again later.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="newsletter-section">
      <div className="container">
        <div className="newsletter-content">
          <h2>Stay Connected</h2>
          <p>Subscribe to our newsletter for exclusive offers and culinary insights</p>
          <form className="newsletter-form" onSubmit={handleSubmit}>
            <input
              type="email"
              placeholder="Enter your email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="newsletter-input"
            />
            <button 
              type="submit" 
              className="btn newsletter-btn"
              disabled={isLoading}
            >
              {isLoading ? 'Subscribing...' : 'Subscribe'}
            </button>
          </form>
          {message && (
            <p className={message.includes('Thank you') ? 'success-message' : 'error-message'}>
              {message}
            </p>
          )}
        </div>
      </div>
    </section>
  );
}

export default Newsletter;