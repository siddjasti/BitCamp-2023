import requests, json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from flask import Flask
app = Flask(__name__)

#reading API keys from json file
with open("key.json", "r") as file:
    data = json.load(file)

account_sid = data["Account_SID"]
auth_token = data["Auth_Token"]
client = Client(account_sid, auth_token)

#Default page for app
@app.route("/")
def hello():
    return "Default Page for Application"

#Answer demo page
@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    resp = VoiceResponse()
    resp.say("Hello there friend!", voice='alice')

    return str(resp)

#Recording an incoming call, waiting for respons
@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    response = VoiceResponse()

    response.say('Hi BitCamp! We are currently recordng this conversation')

    response.record(timeout = 60)

    return str(response)

#run
if __name__ == "__main__":
    app.run(debug=True, port=5000)


