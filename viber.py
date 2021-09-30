import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)

address_api_itilium = os.environ['AddressApiItilium']
login_itilium = os.environ['LoginItilium']
password_itilium = os.environ['PasswordItilium']
auth_key = os.environ['AuthKey']

viber = Api(BotConfiguration(
    name='Itilium-bot',
    avatar='http://site.com/avatar.jpg',
    auth_token=auth_key
))


@app.route('/', methods=['GET'])
def setWebHook():
            viber = Api(BotConfiguration(
                name='Itilium-bot',
                avatar='http://site.com/avatar.jpg',
                auth_token=auth_key
                ))
            viber.unset_webhook()
            viber.set_webhook(request.url)
    except Exception as e:
        return "Failed"
    return "Success"



@app.route('/' + auth_key, methods=['POST'])
def IncomingConnectionPost():
    print("new message")
 #   if request.headers.get('content-type') == 'application/json':
 #       json_string = request.get_data().decode('utf-8')
#
 #       update = json.loads(json_string)
#
 #       print("UnJSONed: " + str(update))
  #      print("update_id: " + str(update["update_id"]))
  #      content = ''
  #      try:
  #          request_itilium = requests.post(address_api_itilium, data=json_string,
  #                                          auth=(login_itilium, password_itilium))
#
#            if request_itilium.status_code == 200 and request_itilium.ok:
#                content = request_itilium.content
#
#                if content != 'Действие не найдено!':
#                    content = json.loads(content)
#        except:
#            print('Error getting data in Itilium')

    return Response(status=200)
