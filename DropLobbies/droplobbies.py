import requests
import json
import base64
import mysql.connector
from mysql.connector import errorcode

def drop_lobbies():
    username = "admin"
    password = "admin"

    message = "bgp-client-name:bgp-client-pw";
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

    response = requests.post(
        "http://blueberry-cake-15306.herokuapp.com/oauth/token?grant_type=password&username={}&password={}".format(username, password),
        headers={"Authorization" : "Basic {}".format(base64_message)}
    )
    data = json.loads(response.content.decode('utf8').replace("'", '"'))

    token = data['access_token']

    users = requests.get("http://blueberry-cake-15306.herokuapp.com/api/users?access_token={}".format(token))

    users = json.loads(users.content.decode('utf8').replace("'", '"'))

    response = requests.get(
        "http://blueberry-cake-15306.herokuapp.com/api/sessions",
        headers={"Bearer": token}
    )

    sessions = json.loads(response.content.decode('utf8').replace("'", '"'))

    print(sessions)

    users_not_touch = ['admin', 'maex', 'joerg', 'hyacinth', 'ryan', 'xox']

    for user in users:
        if user['name'] not in users_not_touch:
            user_token_response = requests.post(
                "http://blueberry-cake-15306.herokuapp.com/oauth/token?grant_type=password&username={}&password={}".format(
                    user['name'], 'abc_123ABC123'),
                headers={"Authorization": "Basic {}".format(base64_message)}
            )
            user_data = json.loads(user_token_response.content.decode('utf8').replace("'", '"'))

            user_token = user_data['access_token']

            for session in sessions['sessions']:
                print(session)
                response = requests.delete(
                        "http://blueberry-cake-15306.herokuapp.com/api/sessions/{}".format(session),
                        headers={"Authorization": "Bearer {}".format(user_token)}
                )

                print(response.content)

if __name__ == '__main__':
    drop_lobbies()

