import React, { useState } from 'react';
import './Reservations.css';
import api from '../services/api';

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
      const payload = {
        customer_name: formData.customer_name,
        email: formData.email,
        phone_number: formData.phone_number,
        number_of_guests: Number(formData.number_of_guests),
        // Send both time_slot and the original fields so backend can accept either
        time_slot: timeSlot,
        date: formData.date,
        time: formData.time,
        special_requests: formData.special_requests,
        newsletter_signup: formData.newsletter_signup,
      };

      const { data } = await api.post('/reservations', payload);

      if (data && data.success) {
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
              <p>Email: reservations@embertable.example</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Reservations;
