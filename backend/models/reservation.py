from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class Reservation(db.Model):
    """Reservation model for Cafe Fausse"""
    __tablename__ = 'reservations'
    
    reservation_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    time_slot = db.Column(db.DateTime, nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    number_of_guests = db.Column(db.Integer, nullable=False, default=2)
    status = db.Column(db.String(20), default='confirmed')  # confirmed, cancelled, completed
    special_requests = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Reservation {self.reservation_id} - Table {self.table_number}>'
    
    def to_dict(self):
        """Convert reservation object to dictionary"""
        return {
            'reservation_id': self.reservation_id,
            'customer_id': self.customer_id,
            'time_slot': self.time_slot.isoformat() if self.time_slot else None,
            'table_number': self.table_number,
            'number_of_guests': self.number_of_guests,
            'status': self.status,
            'special_requests': self.special_requests,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
