import tkinter as tk
from tkinter import ttk, messagebox
from analyzer import analyze_password
from wordlist import generate_wordlist

def launch_gui():
    root = tk.Tk()
    root.title("Password Security Tool")
    root.geometry("520x380")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 11), padding=6)
    style.configure("TLabel", font=("Arial", 11))

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    # TAB 1 — Password Analyzer
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Password Strength Analyzer")

    password_label = ttk.Label(tab1, text="Enter Password:")
    password_label.pack(pady=(15, 5))

    password_entry = ttk.Entry(tab1, show="*", width=40, font=("Arial", 12))
    password_entry.pack(pady=5)

    show_var = tk.BooleanVar()
    def toggle_password():
        password_entry.config(show="" if show_var.get() else "*")

    show_checkbox = ttk.Checkbutton(tab1, text="Show Password", variable=show_var, command=toggle_password)
    show_checkbox.pack(pady=3)

    strength_bar = ttk.Progressbar(tab1, length=350, mode="determinate")
    strength_bar.pack(pady=10)

    strength_label = ttk.Label(tab1, text="", font=("Arial", 12))
    strength_label.pack(pady=4)

    def analyze_now():
        pwd = password_entry.get()
        if not pwd:
            messagebox.showerror("Error", "Please enter a password")
            return

        score = analyze_password(pwd)
        strength_bar["value"] = (score / 6) * 100

        if score <= 2:
            strength_label.config(text="Very Weak ❌", foreground="red")
        elif score <= 4:
            strength_label.config(text="Moderate ⚠️", foreground="orange")
        else:
            strength_label.config(text="Strong 💪", foreground="green")

        messagebox.showinfo("Report", "Password analysis complete.")

    ttk.Button(tab1, text="Analyze Password", command=analyze_now).pack(pady=10)

    # TAB 2 — Wordlist Generator
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Wordlist Generator")

    ttk.Label(tab2, text="Name:").pack(pady=(15, 3))
    name_entry = ttk.Entry(tab2, width=40)
    name_entry.pack(pady=5)

    ttk.Label(tab2, text="DOB (e.g. 2002):").pack(pady=(5, 3))
    dob_entry = ttk.Entry(tab2, width=40)
    dob_entry.pack(pady=5)

    ttk.Label(tab2, text="Pet Name:").pack(pady=(5, 3))
    pet_entry = ttk.Entry(tab2, width=40)
    pet_entry.pack(pady=5)

    def create_wordlist():
        name = name_entry.get()
        dob = dob_entry.get()
        pet = pet_entry.get()

        if not (name or dob or pet):
            messagebox.showerror("Error", "Please enter at least one field")
            return

        generate_wordlist(name, dob, pet)
        messagebox.showinfo("Success", "Wordlist successfully generated!")

    ttk.Button(tab2, text="Generate Wordlist", command=create_wordlist).pack(pady=15)

    root.mainloop()
