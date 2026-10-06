from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class Customer(db.Model):
    """Customer model for Ember"""
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    newsletter_signup = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with reservations
    reservations = db.relationship('Reservation', backref='customer', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Customer {self.customer_name}>'

    def to_dict(self):
        """Convert customer object to dictionary"""
        return {
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'newsletter_signup': self.newsletter_signup,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
