# Call Recording Service using Twilio API

This is a Python application that uses the Twilio API to record incoming and outgoing phone calls. The application consists of three files:

1. `GUI.py` - a graphical user interface (GUI) created using the tkinter python library. This file allows the user to select whether they want to record an incoming call or an outgoing call with two buttons and a phone number input.

2. `RecordCallAPI.py` - this file contains the code for making an outgoing phone call and recording it using the Twilio API.

3. `VoiceAPI.py` - this file contains the code for answering an incoming phone call and recording it using the Twilio API.

The application uses a Flask server to handle incoming calls and record them using the Twilio API. It also uses ngrok to create a temporary link between the Flask server and the Twilio API.

## Requirements

To run this application, you need to have the following installed on your system:

- Python 3.x
- The `requests`, `json`, `twilio`, `tkinter`, and `flask` libraries
- An account on the Twilio platform
- An ngrok account

## Usage

1. Clone this repository to your local machine.

2. Install the required libraries by running the following command in your terminal: (pip instead of pip3 if you don't have python 3.0)

```bash
pip3 install requests json twilio tkinter flask
```

3. Create an account on the Twilio platform and note down your `Account SID` and `Auth Token`.

4. Create a new file called `key.json` in the root directory of the project, and add your Twilio API keys to the json file as follows:

```json
{
"Account_SID": "YOUR_ACCOUNT_SID",
"Auth_Token": "YOUR_AUTH_TOKEN"
}
```

5. Create an account on ngrok and download the ngrok executable file.

6. Open a terminal window and navigate to the directory where the project is saved.

7. In a new terminal window, navigate to the directory where the ngrok executable file is saved, and run the following command:

```bash
./ngrok http 5000
```

This will create a temporary link between your localhost port and the ngrok server. The server will then provide a temporary link which you can put into the TwilioAPI with the phone number you register, so everytime the phone number is called it will run that link

8. In the first terminal window, run the following command to start the Flask server:

```bash
python3 VoiceAPI.py
```

9. In a new terminal window, run the following command to start the GUI:

```python
python3 GUI.py
```

10. Use the GUI to select whether you want to record an incoming call or an outgoing call.

11. Follow the instructions on the GUI to make or receive a call, and the call will be recorded and saved in your Twilio account.
