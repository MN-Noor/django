import firebase_admin
from firebase_admin import credentials,firestore
cred=credentials.Certificate('guidemate.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://guidemate-98eb8.firebaseio.com'
})

db = firestore.client()
