from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pyrebase
from django.conf import settings 
firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
auth = firebase.auth()
database = firebase.database()

@api_view(['POST'])
def sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return Response({"email": email, "idToken": session_id}, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Error: {e}")
        return Response({"error": "Invalid Credentials! Please check your data."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sign_up(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')

    try:
        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        database.child("users").child(uid).set({"name": name, "email": email})
        return Response({"message": "Registration successful! Please log in."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(f"Error: {e}")
        return Response({"error": "Registration failed! Please try again."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        return Response({"error": "User is not logged in."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

# Create your views here.
