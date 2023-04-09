import requests, json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from flask import Flask
app = Flask(__name__)

with open("key.json", "r") as file:
    data = json.load(file)

account_sid = data["Account_SID"]
auth_token = data["Auth_Token"]
client = Client(account_sid, auth_token)

@app.route("/")
def hello():
    return "Default Page for Application"

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()
    # Read a message aloud to the caller
    resp.say("Hello there friend!", voice='alice')

    return str(resp)

@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say('Hey we are currently recording')

    # Use <Record> to record the caller's message
    response.record(timeout = 60)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)


