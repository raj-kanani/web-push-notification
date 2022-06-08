# pass toast notification
from plyer import notification

if __name__ == '__main__':
    notification.notify(title='this is demo notification',
                        message='hello successfully notification pass',
                        # app_icon="/home/rajkplutus/PycharmProjects/send-notification/myproject/icon.ico/",
                        timeout=5)
from typing import List


# def new(request):
#     color = ['a', 'b', 'c']
#     my_color = [c for c in color if c == 'a']
