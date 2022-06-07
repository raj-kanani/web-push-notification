import pyrebase

# login and register with email pwd in firebase database.
firebaseconfig = {

    "apiKey": "AIzaSyBT9W25iRXt87JtWgfbDDKGlzhXPEN3MWc",
    "authDomain": "python-program-66e96.firebaseapp.com",
    "databaseURL": "https://python-program-66e96-default-rtdb.firebaseio.com/",
    "projectId": "python-program-66e96",
    "storageBucket": "python-program-66e96.appspot.com",
    "messagingSenderId": "282806100614",
    'appId': "1:282806100614:web:5519c6d029a68df25be707",
    "measurementId": "G-PE9503T7QB"
}

firebase = pyrebase.initialize_app(firebaseconfig)
#
# connect to the database
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

# # login user
# email = input("enter your email:- ")
# password = input("enter your password:- ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("success login")
# except:
#     print("invalid")

# # # register
email = input('enter email :- ')
password = input('enter password:- ')
confirm = input('enter confirm pwd:- ')
try:
    if password == confirm:
        auth.create_user_with_email_and_password(email, password)
        print('register success')
except:
    print('Email already exist')


# firebase  mobile push notification
# import requests
# import json
#
# serverToken = '282806100614'
# deviceToken = ''
#
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'key=' + serverToken,
# }
#
# body = {
#     'notification': {'title': 'Sending push form python script',
#                      'body': 'New Message'
#                      },
#     'to':
#         deviceToken,
#     'priority': 'high',
#     #   'data': dataPayLoad,
# }
# response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
# print(response.status_code)
#
# print(response.json())
