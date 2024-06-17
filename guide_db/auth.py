# views.py
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .serializers import SignInSerializer, SignUpSerializer
from  backend import settings

API_KEY = settings.FIREBASE_CONFIG.get('apiKey')

@csrf_exempt
@api_view(['POST'])
def sign_up(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        details = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        response = requests.post(
            f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}',
            json=details
        )
        response_data = response.json()
        if 'error' in response_data:
            error_message = response_data['error']['message']
            return Response({'status': 'error', 'message': error_message}, status=status.HTTP_400_BAD_REQUEST)
        if 'idToken' in response_data:
            return Response({'status': 'success', 'idToken': response_data['idToken']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def sign_in(request):
    serializer = SignInSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        details = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }
        response = requests.post(
            f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}',
            json=details
        )
        response_data = response.json()
        if 'error' in response_data:
            error_message = response_data['error']['message']
            return Response({'status': 'error', 'message': error_message}, status=status.HTTP_400_BAD_REQUEST)
        if 'idToken' in response_data:
            return Response({'status': 'success', 'idToken': response_data['idToken']}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def logout(request):
    try:
        del request.session['uid']
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    except KeyError:
        return Response({"error": "User is not logged in."}, status=status.HTTP_400_BAD_REQUEST)
