import requests
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import *


def home(request):
    return render(request, 'index.html', {
        'room_name': "broadcast"
    })


# web socket notification
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")


#  firebase notification


def send_notification(registration_ids, message_title, message_desc):
    fcm_api = '282806100614'
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key=' + fcm_api}

    payload = {
        "registration_ids": registration_ids,
        "priority": "high",
        "notification": {
            "body": message_desc,
            "title": message_title,

        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result.json())


def send(request):
    resgistration = ['BFpts-G9B_Ivup2QJxLVBT2-jRDqYVDOFZbv01IST9F1iYS1p5hPagwokUz4jp5ttjiyeGKsRBUMp5OfveLWuV8']
    send_notification(resgistration, 'raj kanani demo message', 'this is demo test')
    return HttpResponse("sent")


def showFirebaseJS(request):
    data = 'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
           'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
           'var firebaseConfig = {' \
           '        apiKey: "AIzaSyBT9W25iRXt87JtWgfbDDKGlzhXPEN3MWc",' \
           '        authDomain: "python-program-66e96.firebaseapp.com",' \
           '        databaseURL: "https://python-program-66e96-default-rtdb.firebaseio.com",' \
           '        projectId: "python-program-66e96",' \
           '        storageBucket: "python-program-66e96.appspot.com",' \
           '        messagingSenderId: "282806100614",' \
           '        appId: "1:282806100614:web:5519c6d029a68df25be707",' \
           '        measurementId: "G-PE9503T7QB"' \
           ' };' \
           'firebase.initializeApp(firebaseConfig);' \
           'const messaging=firebase.messaging();' \
           'messaging.setBackgroundMessageHandler(function (payload) {' \
           '    console.log(payload);' \
           '    const notification=JSON.parse(payload);' \
           '    const notificationOption={' \
           '        body:notification.body,' \
           '        icon:notification.icon' \
           '    };' \
           '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
           '});'

    return HttpResponse(data, content_type="text/javascript")


