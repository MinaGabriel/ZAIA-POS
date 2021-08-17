from django.http.response import JsonResponse
from django.shortcuts import render
import pyrebase
import json
import requests.exceptions   # error types

firebaseConfig = {
    "apiKey": "AIzaSyCkOpYTEqo_m_OiPdZL9mKw5NFYFMgA1QU",
    "authDomain": "zaia-pos.firebaseapp.com",
    "projectId": "zaia-pos",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "zaia-pos.appspot.com",
    "messagingSenderId": "198095119811",
    "appId": "1:198095119811:web:638fd72c863ba6855c0976",
    "measurementId": "G-X2DZNB4VNH"
}

# Initializing database,auth and firebase for further use
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

# Create your views here.

def sign_up(request):
    return render(request, 'authentication-signup-cover.html')


def verify_email(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = request.POST.get('password')
    
    try:
        # creating a user with the given email and password
        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        print(user)
        print(uid)
    except requests.exceptions.HTTPError as httpErr:
        error_message = json.loads(httpErr.args[1])['error']['message']
        # if email exists 
        if error_message == 'EMAIL_EXISTS': 
            return render(request, 'authentication-email-exists.html', {'email': email})
        print(error_message)
        return render(request, 'authentication-signup-cover.html', {'error': error_message})
    
    print(email, ' and password is', password)
    return render(request, 'authentication-email-verification-basic.html')

def sign_in(request):
    return render(request, 'authentication-signin-cover.html')