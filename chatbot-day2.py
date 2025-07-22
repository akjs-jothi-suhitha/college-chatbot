import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "admission" in user_input:
        return "Admission details are available on the college website."
    elif "courses" in user_input:
        return "We offer B.Tech, M.Tech and more. Visit our website for full list."
    elif "fees" in user_input:
        return "Fee structure varies by course. Check the fee section online."
    elif "thank you" in user_input or "thanks" in user_input:
        return "Always happy to help!"
    else:
        return "Sorry, I didn't understand that. Please ask something else."
def format_message(sender, message):
    time_now = datetime.now().strftime("%I:%M %p")
    return f"{sender} ({time_now}): {message}"
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, format_message("User", user_input) + "\n")
    user_entry.delete(0, tk.END)
    bot_response = get_bot_response(user_input)
    chat_log.insert(tk.END, format_message("Bot", bot_response) + "\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
root = tk.Tk()
root.title("College Chatbot Assistant - Day 2")
root.geometry("480x520")
root.resizable(False, False)
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, state=tk.DISABLED, font=("Arial", 10))
user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
send_button = tk.Button(root, text="Send", width=10, command=send_message, bg="#4CAF50", fg="white")
send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))
root.mainloop()
