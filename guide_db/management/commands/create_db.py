from django.core.management.base import BaseCommand
from guide_db.firebase import db
# from firebase import db
from datetime import datetime

class Command(BaseCommand):
    help = 'Initialize Firestore collections with sample data'

    def handle(self, *args, **kwargs):
        # Users collection
        users_ref = db.collection('Users').document('user_1')
        users_ref.set({
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'hashed_password',
            'contact_details': '123456789',
            'user_type': 'Tourist',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Profiles collection
        profiles_ref = db.collection('Profiles').document('profile_1')
        profiles_ref.set({
            'user_id': 'user_1',
            'expertise': 'Expert in local history',
            'languages_spoken': 'English, Spanish',
            'availability': 'Weekends',
            'profile_picture': 'path/to/picture.jpg',
            'security_details': 'Background checked',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Trips collection
        trips_ref = db.collection('Trips').document('trip_1')
        trips_ref.set({
            'guide_id': 'guide_1',
            'trip_name': 'City Tour',
            'description': 'A comprehensive tour of the city',
            'itinerary': 'Start at the museum, end at the park',
            'availability': 'Weekends',
            'price': 100,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Bookings collection
        bookings_ref = db.collection('Bookings').document('booking_1')
        bookings_ref.set({
            'user_id': 'user_1',
            'trip_id': 'trip_1',
            'number_of_participants': 5,
            'total_cost': 500,
            'status': 'Pending',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Reviews collection
        reviews_ref = db.collection('Reviews').document('review_1')
        reviews_ref.set({
            'user_id': 'user_1',
            'guide_id': 'guide_1',
            'rating': 5,
            'review_text': 'Great experience!',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Payments collection
        payments_ref = db.collection('Payments').document('payment_1')
        payments_ref.set({
            'booking_id': 'booking_1',
            'amount': 500,
            'payment_method': 'Credit Card',
            'payment_status': 'Completed',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Advertisements collection
        advertisements_ref = db.collection('Advertisements').document('advertisement_1')
        advertisements_ref.set({
            'profile_id': 'profile_1',
            'image_path': 'path/to/image.jpg',
            'description': 'Best tour guide in town!',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        # Timelines collection
        timelines_ref = db.collection('Timelines').document('timeline_1')
        timelines_ref.set({
            'guide_id': 'guide_1',
            'available_from': datetime(2024, 6, 20),
            'available_to': datetime(2024, 6, 30),
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
        })

        self.stdout.write(self.style.SUCCESS('Firestore initialized with sample data'))
