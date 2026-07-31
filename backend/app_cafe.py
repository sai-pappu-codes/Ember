from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random
import re

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/cafe_fausse_dev')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'cafe-fausse-secret-key-change-in-production')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Models
class Customer(db.Model):
    """Customer model for Cafe Fausse"""
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
    
    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'newsletter_signup': self.newsletter_signup,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Reservation(db.Model):
    """Reservation model for Cafe Fausse"""
    __tablename__ = 'reservations'
    
    reservation_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    time_slot = db.Column(db.DateTime, nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    number_of_guests = db.Column(db.Integer, nullable=False, default=2)
    status = db.Column(db.String(20), default='confirmed')
    special_requests = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'reservation_id': self.reservation_id,
            'customer_id': self.customer_id,
            'time_slot': self.time_slot.isoformat() if self.time_slot else None,
            'table_number': self.table_number,
            'number_of_guests': self.number_of_guests,
            'status': self.status,
            'special_requests': self.special_requests,
            'customer': self.customer.to_dict() if self.customer else None
        }

# Helper functions
def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_table_availability(time_slot, number_of_guests):
    """Check if tables are available for the given time slot"""
    # Restaurant has 30 tables total
    # Check reservations within 2 hours of the requested time
    start_time = time_slot - timedelta(hours=1)
    end_time = time_slot + timedelta(hours=1)
    
    existing_reservations = Reservation.query.filter(
        Reservation.time_slot.between(start_time, end_time),
        Reservation.status == 'confirmed'
    ).all()
    
    occupied_tables = [r.table_number for r in existing_reservations]
    available_tables = [i for i in range(1, 31) if i not in occupied_tables]
    
    # Check if we have enough tables for the party size
    # Assume each table can accommodate up to 4 guests
    tables_needed = (number_of_guests + 3) // 4  # Round up division
    
    if len(available_tables) >= tables_needed:
        return available_tables[:tables_needed]
    return None

# Routes
@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Cafe Fausse API is running",
        "restaurant": "Cafe Fausse - Fine Dining Experience"
    }), 200

@app.route('/api')
def api_home():
    """API home endpoint"""
    return jsonify({
        "message": "Welcome to Cafe Fausse API",
        "version": "1.0.0",
        "restaurant_info": {
            "name": "Cafe Fausse",
            "address": "1234 Culinary Ave, Suite 100, Washington, DC 20002",
            "phone": "(202) 555-4567",
            "hours": {
                "monday_saturday": "5:00 PM - 11:00 PM",
                "sunday": "5:00 PM - 9:00 PM"
            }
        },
        "endpoints": {
            "/api/health": "Health check",
            "/api": "API information",
            "/api/menu": "Get menu items",
            "/api/reservations": "Make a reservation",
            "/api/reservations/<id>": "Get reservation details",
            "/api/newsletter": "Newsletter signup",
            "/api/gallery": "Get gallery items",
            "/api/reviews": "Get customer reviews"
        }
    }), 200

@app.route('/api/menu')
def get_menu():
    """Get restaurant menu"""
    menu = {
        "starters": [
            {
                "id": 1,
                "name": "Bruschetta",
                "description": "Fresh tomatoes, basil, olive oil, and toasted baguette slices",
                "price": 8.50,
                "category": "starters",
                "image": "/images/bruschetta.jpg"
            },
            {
                "id": 2,
                "name": "Caesar Salad",
                "description": "Crisp romaine with homemade Caesar dressing",
                "price": 9.00,
                "category": "starters",
                "image": "/images/caesar-salad.jpg"
            }
        ],
        "main_courses": [
            {
                "id": 3,
                "name": "Grilled Salmon",
                "description": "Served with lemon butter sauce and seasonal vegetables",
                "price": 22.00,
                "category": "main_courses",
                "image": "/images/grilled-salmon.jpg"
            },
            {
                "id": 4,
                "name": "Ribeye Steak",
                "description": "12 oz prime cut with garlic mashed potatoes",
                "price": 28.00,
                "category": "main_courses",
                "image": "/images/ribeye-steak.jpg"
            },
            {
                "id": 5,
                "name": "Vegetable Risotto",
                "description": "Creamy Arborio rice with wild mushrooms",
                "price": 18.00,
                "category": "main_courses",
                "vegetarian": True,
                "image": "/images/vegetable-risotto.jpg"
            }
        ],
        "desserts": [
            {
                "id": 6,
                "name": "Tiramisu",
                "description": "Classic Italian dessert with mascarpone",
                "price": 7.50,
                "category": "desserts",
                "image": "/images/tiramisu.jpg"
            },
            {
                "id": 7,
                "name": "Cheesecake",
                "description": "Creamy cheesecake with berry compote",
                "price": 7.00,
                "category": "desserts",
                "image": "/images/cheesecake.jpg"
            }
        ],
        "beverages": [
            {
                "id": 8,
                "name": "Red Wine (Glass)",
                "description": "A selection of Italian reds",
                "price": 10.00,
                "category": "beverages"
            },
            {
                "id": 9,
                "name": "White Wine (Glass)",
                "description": "Crisp and refreshing",
                "price": 9.00,
                "category": "beverages"
            },
            {
                "id": 10,
                "name": "Craft Beer",
                "description": "Local artisan brews",
                "price": 6.00,
                "category": "beverages"
            },
            {
                "id": 11,
                "name": "Espresso",
                "description": "Strong and aromatic",
                "price": 3.00,
                "category": "beverages"
            }
        ]
    }
    return jsonify(menu), 200

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    """Create a new reservation"""
    data = request.get_json() or {}

    # Validate required top-level fields (allow time_slot OR date+time)
    base_required = ['customer_name', 'email', 'number_of_guests']
    for field in base_required:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Coerce and validate number_of_guests
    try:
        number_of_guests = int(data.get('number_of_guests'))
    except (TypeError, ValueError):
        return jsonify({"error": "Number of guests must be an integer between 1 and 12"}), 400
    if number_of_guests < 1 or number_of_guests > 12:
        return jsonify({"error": "Number of guests must be between 1 and 12"}), 400

    # Validate email
    if not validate_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Parse time slot - accept ISO time_slot OR date+time in various formats
    date_str = data.get('date')
    time_str = data.get('time')

    # Helper to normalize date
    def normalize_date(ds: str) -> str:
        if ds is None:
            return None
        if '.' in ds:
            # Support DD.MM.YYYY
            try:
                d, m, y = ds.split('.')
                return f"{y}-{m.zfill(2)}-{d.zfill(2)}"
            except Exception:
                return None
        return ds  # Assume already YYYY-MM-DD

    # Build candidate strings to try parsing
    candidates = []
    if data.get('time_slot'):
        candidates.append(data.get('time_slot'))
    nd = normalize_date(date_str)
    if nd and time_str:
        tnorm = time_str if len(time_str.split(':')) == 3 else f"{time_str}:00"
        candidates.append(f"{nd}T{tnorm}")

    if not candidates:
        return jsonify({"error": "Missing required field: time_slot (or provide date and time)"}), 400

    time_slot = None
    parse_error = None
    for cand in candidates:
        try:
            time_slot = datetime.fromisoformat(cand)
            break
        except Exception as e:
            parse_error = e
            continue

    if time_slot is None:
        return jsonify({"error": "Invalid time format. Use YYYY-MM-DD or DD.MM.YYYY with HH:MM"}), 400

    # Check restaurant hours
    hour = time_slot.hour
    day_of_week = time_slot.weekday()

    # Monday-Saturday: 5PM-11PM (17:00-23:00)
    # Sunday: 5PM-9PM (17:00-21:00)
    if day_of_week == 6:  # Sunday
        if hour < 17 or hour > 21:
            return jsonify({"error": "Restaurant is closed at this time. Sunday hours: 5:00 PM - 9:00 PM"}), 400
    else:
        if hour < 17 or hour > 23:
            return jsonify({"error": "Restaurant is closed at this time. Monday-Saturday hours: 5:00 PM - 11:00 PM"}), 400

    # Check table availability
    available_tables = check_table_availability(time_slot, number_of_guests)
    if not available_tables:
        return jsonify({
            "error": "No tables available for this time slot. Please choose another time.",
            "status": "unavailable"
        }), 400

    try:
        # Check if customer exists
        customer = Customer.query.filter_by(email=data['email']).first()
        if not customer:
            # Create new customer
            customer = Customer(
                customer_name=data['customer_name'],
                email=data['email'],
                phone_number=data.get('phone_number'),
                newsletter_signup=data.get('newsletter_signup', False)
            )
            db.session.add(customer)
            db.session.flush()

        # Create reservation (assign a random available table)
        reservation = Reservation(
            customer_id=customer.customer_id,
            time_slot=time_slot,
            table_number=random.choice(available_tables),
            number_of_guests=number_of_guests,
            special_requests=data.get('special_requests')
        )
        db.session.add(reservation)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Reservation confirmed!",
            "reservation": reservation.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations/<int:reservation_id>')
def get_reservation(reservation_id):
    """Get reservation details"""
    reservation = Reservation.query.get_or_404(reservation_id)
    return jsonify(reservation.to_dict()), 200

@app.route('/api/newsletter', methods=['POST'])
def newsletter_signup():
    """Newsletter signup"""
    data = request.get_json()
    
    if 'email' not in data:
        return jsonify({"error": "Email is required"}), 400
    
    if not validate_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400
    
    try:
        # Check if customer exists
        customer = Customer.query.filter_by(email=data['email']).first()
        if customer:
            customer.newsletter_signup = True
            message = "Email updated for newsletter"
        else:
            # Create new customer for newsletter
            customer = Customer(
                customer_name=data.get('name', 'Newsletter Subscriber'),
                email=data['email'],
                newsletter_signup=True
            )
            db.session.add(customer)
            message = "Successfully subscribed to newsletter"
        
        db.session.commit()
        return jsonify({"success": True, "message": message}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/gallery')
def get_gallery():
    """Get gallery items"""
    gallery = {
        "images": [
            {
                "id": 1,
                "url": "/images/restaurant-interior.jpg",
                "caption": "Elegant dining room",
                "category": "interior"
            },
            {
                "id": 2,
                "url": "/images/chef-antonio.jpg",
                "caption": "Chef Antonio Rossi",
                "category": "team"
            },
            {
                "id": 3,
                "url": "/images/special-event.jpg",
                "caption": "Private event hosting",
                "category": "events"
            }
        ],
        "awards": [
            {
                "year": 2022,
                "title": "Culinary Excellence Award",
                "organization": "DC Restaurant Association"
            },
            {
                "year": 2023,
                "title": "Restaurant of the Year",
                "organization": "Washington Food Critics"
            },
            {
                "year": 2023,
                "title": "Best Fine Dining Experience",
                "organization": "Foodie Magazine"
            }
        ]
    }
    return jsonify(gallery), 200

@app.route('/api/reviews')
def get_reviews():
    """Get customer reviews"""
    reviews = [
        {
            "id": 1,
            "author": "Gourmet Review",
            "text": "Exceptional ambiance and unforgettable flavors.",
            "rating": 5,
            "date": "2023-10-15"
        },
        {
            "id": 2,
            "author": "The Daily Bite",
            "text": "A must-visit restaurant for food enthusiasts.",
            "rating": 5,
            "date": "2023-09-20"
        }
    ]
    return jsonify(reviews), 200

@app.route('/api/check-availability', methods=['POST'])
def check_availability():
    """Check table availability for a specific time"""
    data = request.get_json()
    
    if 'time_slot' not in data or 'number_of_guests' not in data:
        return jsonify({"error": "time_slot and number_of_guests are required"}), 400
    
    try:
        time_slot = datetime.fromisoformat(data['time_slot'])
    except:
        return jsonify({"error": "Invalid time format"}), 400
    
    available_tables = check_table_availability(time_slot, data['number_of_guests'])
    
    return jsonify({
        "available": bool(available_tables),
        "tables_available": len(available_tables) if available_tables else 0,
        "message": "Tables available" if available_tables else "No tables available for this time"
    }), 200

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
