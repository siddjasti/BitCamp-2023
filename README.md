Readme for Call Recording Service using Twilio API
This is a Python application that uses the Twilio API to record incoming and outgoing phone calls. The application consists of three files:

call_recording_gui.py - a graphical user interface (GUI) created using the tkinter library. This file allows the user to select whether they want to record an incoming call or an outgoing call.

RecordCallAPI.py - this file contains the code for making an outgoing phone call and recording it using the Twilio API.

VoiceAPI.py - this file contains the code for answering an incoming phone call and recording it using the Twilio API.

The application uses a Flask server to handle incoming calls and record them using the Twilio API. It also uses ngrok to create a temporary link between the Flask server and the Twilio API.

Requirements
To run this application, you need to have the following installed on your system:

Python 3.x
The requests, json, twilio, tkinter, and flask libraries
An account on the Twilio platform
An ngrok account

Usage
Open a terminal window and navigate to the directory where the project is saved.

In a new terminal window, navigate to the directory where the ngrok executable file is saved, and run the following command:

bash
Copy code
./ngrok http 5000
This will create a temporary link between your localhost and the Twilio API.

In the first terminal window, run the following command to start the Flask server:

Copy code
python3 VoiceAPI.py
In a new terminal window, run the following command to start the GUI:

Copy code
python3 call_recording_gui.py
Use the GUI to select whether you want to record an incoming call or an outgoing call.

Follow the instructions on the GUI to make or receive a call, and the call will be recorded and saved in your Twilio account.
