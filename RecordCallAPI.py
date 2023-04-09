import os, requests, json
from twilio.rest import Client

with open("key.json", "r") as file:
    data = json.load(file)

account_sid = data["Account_SID"]
auth_token = data["Auth_Token"]
client = Client(account_sid, auth_token)

call = client.calls.create(
                        record=True,
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+19138089997',
                        from_='+15075744740'
                    )

print(call.sid)