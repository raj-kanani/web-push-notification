# # import scopes
# # from oauth2client.service_account import ServiceAccountCredentials
# #
# #
# # def _get_access_token():
# #     """Retrieve a valid access token that can be used to authorize requests.
# #
# #     :return: Access token.
# #     """
# #     credentials = ServiceAccountCredentials.from_json_keyfile_name(
# #         'service-account.json', scopes)
# #     access_token_info = credentials.get_access_token()
# #     return access_token_info.access_token
#
#
# import requests
# import json
#
# serverToken = '282806100614'
# deviceToken = 'BFpts-G9B_Ivup2QJxLVBT2-jRDqYVDOFZbv01IST9F1iYS1p5hPagwokUz4jp5ttjiyeGKsRBUMp5OfveLWuV8'
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
# # print(response.json())


# pass toast notification
from plyer import notification

if __name__ == '__main__':
    notification.notify(title='this is demo notification',
                        message='hello successfully notification pass',
                        # app_icon="/home/rajkplutus/PycharmProjects/send-notification/myproject/icon.ico/",
                        timeout=5)
