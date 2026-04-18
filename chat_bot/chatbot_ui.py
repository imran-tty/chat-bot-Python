import tkinter as tk
from chatbot_backend import get_response
window = tk.Tk()
window.title("FIFA Chatbot ⚽")
window.geometry("500x500")
chat_box = tk.Text(window, height=20, width=60)
chat_box.pack(pady=10)


entry = tk.Entry(window, width=40)
entry.pack(pady=10)
def send_message():
    user_text = entry.get()
    chat_box.insert(tk.END, "You: " + user_text + "\n")

    bot_response = get_response(user_text)
    chat_box.insert(tk.END, "Bot: " + bot_response + "\n\n")

    entry.delete(0, tk.END)
send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack()

window.mainloop()
