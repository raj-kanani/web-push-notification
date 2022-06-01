from .models import *


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {'notifications': allnotifications}
