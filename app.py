import tkinter as tk
from tkinter import scrolledtext
from emotion_detector import detect_emotion
from responses import responses

def chatbot_reply():
    user_text = user_input.get()
    chat_area.insert(tk.END, "You: " + user_text + "\n")

    emotion = detect_emotion(user_text)
    reply = responses[emotion][0]

    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
    user_input.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Mental Health Chatbot")
root.geometry("500x500")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.pack(pady=10)
chat_area.insert(tk.END, "Bot: Hello! I’m here to listen 😊\n\n")

user_input = tk.Entry(root, width=50)
user_input.pack(pady=5)

send_button = tk.Button(root, text="Send", command=chatbot_reply)
send_button.pack()

root.mainloop()