import os, requests, json
from twilio.rest import Client
import tkinter as tk

#read and set the API keys from json file
with open("key.json", "r") as file:
    data = json.load(file)
account_sid = data["Account_SID"]
auth_token = data["Auth_Token"]
client = Client(account_sid, auth_token)

#defining what happens when we want tos make a call
def make_call():
    to_number = to_entry.get()

    call = client.calls.create(
        to=to_number,
        from_='+15075744740',
        url='http://demo.twilio.com/docs/voice.xml',
        record=True
    )
    print(call.sid)

# GUI table
root = tk.Tk()
root.title("Make a Phone Call")

#GU button binding and implementation
to_label = tk.Label(root, text="Enter phone number:")
to_label.pack(padx=20, pady=10)
to_entry = tk.Entry(root, width=20)
to_entry.pack(padx=20, pady=10)

call_button = tk.Button(root, text="Call", command=make_call,  activebackground="black", activeforeground="white")
call_button.pack(padx=20, pady=10)

#run
root.mainloop()