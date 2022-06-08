# import requests
# import json
#
# serverToken = ''
# deviceToken = ''
#
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'key=' + serverToken,
# }
#
# body = {
#     'notification': {'title': 'Testing notification',
#                      'body': 'Hii this is a testing'
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

