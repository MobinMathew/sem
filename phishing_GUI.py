import tkinter as tk

root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# GUI Component
label = tk.Label(root, text="Enter url:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)
