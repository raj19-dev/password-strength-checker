from password_checker import log_entry, check_password, generate_password
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Password Strength Checker")
width = 450
height = 420
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(True, True)
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1e1e2f")
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 10))
style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.configure("TRadiobutton", background="#1e1e2f", foreground="white")
main_frame = ttk.Frame(window)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)
title_label = ttk.Label(main_frame, text="Password Strength Checker", style="Title.TLabel")
title_label.pack(pady=10)
mode = tk.StringVar(value="check")
check_radio = ttk.Radiobutton(main_frame, text="Check Password", variable=mode, value="check")
check_radio.pack()
generate_radio = ttk.Radiobutton(main_frame, text="Generate Password", variable=mode, value="generate")
generate_radio.pack()
password_label = ttk.Label(main_frame, text="Enter Password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(main_frame, show="*")
password_entry.pack(pady=5)
def block_spaces(event):
    if event.char == " ":
        return "break"
password_entry.bind("<KeyPress>", block_spaces)
length_label = ttk.Label(main_frame, text="Enter Length (min. 8):")
length_label.pack(pady=5)
length_entry = ttk.Entry(main_frame)
length_entry.pack(pady=5)
result_label = tk.Label(
    main_frame,
    text="",
    bg="#1e1e2f",
    fg="white",
    wraplength=380,
    justify="left",
    font=("Segoe UI", 10)
)
result_label.pack(pady=15)
def check():
    password = password_entry.get()
    if not password.strip():
        result_label.config(text = "Please enter a password.", fg = "#ff4d4d")
        return
    strength, missing, message = check_password(password)
    if strength is None:
        result_label.config(text=message, fg="#ff4d4d")
        return
    display_text = message + "\n"
    display_text += "Strength: " + strength + "\n"
    if missing:
        display_text += "Missing: " + ", ".join(missing)
    else:
        display_text += "Missing: None"
    if strength == "Weak":
        result_label.config(text=display_text, fg="#ff4d4d")
    elif strength == "Medium":
        result_label.config(text=display_text, fg="#ffa500")
    else:
        result_label.config(text=display_text, fg="#00cc66")

    log_entry("Checked", password, strength, missing, len(password))
def generate():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="#ff4d4d")
        return
    if length < 8:
        result_label.config(text="Length must be at least 8 characters.", fg="#ff4d4d")
        return
    final_password = generate_password(length)
    result_label.config(
        text="Generated Password:\n" + final_password,
        fg="#4da6ff"
    )
    log_entry("Generated", final_password, "Strong", None, length)
def execute():
    if mode.get() == "check":
        check()
    else:
        generate()
submit_button = ttk.Button(main_frame, text="Submit", command=execute)
submit_button.pack(pady=10)
window.mainloop()