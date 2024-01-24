import tkinter as tk
from tkinter import ttk
import webview
import threading

def open_url():
    url = entry.get()

    webview.create_window('IsaacBrowse', url)
    webview.start()

app = tk.Tk()
app.title("IsaacBrowse")
app.geometry("800x600")

address_frame = tk.Frame(app)
address_frame.pack(pady=10)

label = tk.Label(address_frame, text="Enter URL:")
label.pack(side=tk.LEFT)

entry = tk.Entry(address_frame, width=50)
entry.pack(side=tk.LEFT)

go_button = tk.Button(address_frame, text="Go", command=open_url)
go_button.pack(side=tk.LEFT)

app.mainloop()
