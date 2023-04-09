import requests, json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Sidd!"

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()
    # Read a message aloud to the caller
    resp.say("Aadit has ADHD and is in love with akansha", voice='Polly.Aditi')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)







#with open("key.json", "r") as file:
#    data = json.load(file)

#account_sid = data["Account_SID"]
#auth_token = data["Auth_Token"]

#client = Client(account_sid, auth_token)

#message = client.messages.create(
    #to="+9138089997", 
    #from_="+9134613920",
    #body="Hi prina pad")
#print(message.sid)

