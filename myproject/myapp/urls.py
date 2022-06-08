from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.test, name="test"),
    # path('send/', views.send, name="send"),
    # path('send-noti/', views.send_notification, name="send-noti"),
    # path('firebase-messaging-sw.js', views.showFirebaseJS, name="show_firebase_js"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
