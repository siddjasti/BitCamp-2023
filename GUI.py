import tkinter as tk
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

# function to run RecordCallAPI
def run_record():
    os.system(f"python3 {dir_path}/RecordCallAPI.py")

# functon to run VoiceAPI
def run_voice():
    os.system(f"python3 {dir_path}/VoiceAPI.py")

root = tk.Tk()

# Set the window title
root.title("Recording Call Service")
root.configure(bg='black')
button_font = ('Courier New', 20, 'bold')

# create incoming button
button1 = tk.Button(root, text="Record Incoming Calls!", font=button_font, compound='left',fg="black", command=run_voice, activebackground="black", activeforeground="white")
button1.pack(padx=20, pady=10)

# create outgoing button
button2 = tk.Button(root, text="Record an Outgoing Call!", font=button_font, compound='left',fg="black", command=run_record, activebackground="black", activeforeground="white")
button2.pack(padx=20, pady=10)

# defining button clicking
def flash_buttons():
    button1.configure(bg='#FFC300')
    button2.configure(bg='#FFC300')
    root.after(200, lambda: button1.configure(bg='#E6E6E6'))
    root.after(200, lambda: button2.configure(bg='#E6E6E6'))

# bind buttons to look like they are clicking
button1.bind('<Button-1>', lambda e: flash_buttons())
button2.bind('<Button-1>', lambda e: flash_buttons())

# run the GUI
root.mainloop()




