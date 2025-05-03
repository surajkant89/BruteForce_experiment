import tkinter as tk
from tkinter import messagebox
import itertools
import string
import threading
import time

def brute_force():
    password = entry_password.get()
    show_guesses = var_show.get()
    include_symbols = var_symbols.get()

    if not password:
        messagebox.showerror("Input Error", "Please enter a password.")
        return

    charset = string.ascii_letters + string.digits
    if include_symbols:
        charset += string.punctuation

    attempts = 0
    found = False
    start_time = time.time()

    btn_start.config(state='disabled')
    status_label.config(text="Cracking password...")

    for length in range(1, len(password) + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            attempts += 1

            if show_guesses:
                guess_label.config(text=f"Trying: {guess_str}")
                root.update()

            if guess_str == password:
                duration = time.time() - start_time
                guess_label.config(text=f"Password: {guess_str}")
                status_label.config(text=f"Cracked in {attempts} attempts | {duration:.2f} sec")
                found = True
                btn_start.config(state='normal')
                return

    status_label.config(text="Password not cracked.")
    btn_start.config(state='normal')

def start_thread():
    threading.Thread(target=brute_force).start()

# GUI Setup
root = tk.Tk()
root.title("Brute Force Password Cracker")

tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

var_show = tk.BooleanVar()
tk.Checkbutton(root, text="Show guesses", variable=var_show).pack()

var_symbols = tk.BooleanVar()
tk.Checkbutton(root, text="Include symbols (!@# etc)", variable=var_symbols).pack()

btn_start = tk.Button(root, text="Start Cracking", command=start_thread)
btn_start.pack(pady=10)

guess_label = tk.Label(root, text="")
guess_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
