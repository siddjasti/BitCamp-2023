import os, requests, json
from twilio.rest import Client
import tkinter as tk

with open("key.json", "r") as file:
    data = json.load(file)

account_sid = data["Account_SID"]
auth_token = data["Auth_Token"]
client = Client(account_sid, auth_token)

def make_call():
    to_number = to_entry.get()

    call = client.calls.create(
        to=to_number,
        from_='+15075744740',
        url='http://demo.twilio.com/docs/voice.xml',
        record=True
    )

    print(call.sid)

root = tk.Tk()
root.title("Make a Phone Call")

to_label = tk.Label(root, text="Enter phone number:")
to_label.pack(padx=20, pady=10)
to_entry = tk.Entry(root, width=20)
to_entry.pack(padx=20, pady=10)

call_button = tk.Button(root, text="Call", command=make_call,  activebackground="black", activeforeground="white")
call_button.pack(padx=20, pady=10)

root.mainloop()