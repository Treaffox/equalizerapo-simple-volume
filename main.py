import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from tkinter import font as tkFont

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {file_path}")
        return None

def save_file(lines, file_path):
    try:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def update_values(new_value):
    global lines
    if lines:
        line = lines[0]
        parts = list(line)
        
        # Format the new value as a string with exactly two characters
        if new_value < 0:
            new_value_str = f"{new_value:2d}"
        else:
            new_value_str = f"{new_value:2d}".replace(' ', '0')
        
        # Modify characters at index 8 and 9
        parts[8] = new_value_str[0]
        parts[9] = new_value_str[1]
        
        lines[0] = ''.join(parts)
        save_file(lines, file_path)
        value_label.config(text=f"AKTUELLE LAUTSTÄRKE: {new_value} DB")

def open_link(event):
    webbrowser.open_new("https://trfx.de")

file_path = r"C:\Program Files\EqualizerAPO\config\config.txt"
lines = load_file(file_path)

if lines:
    root = tk.Tk()
    root.title("CONFIG UPDATER")

    # Load Kode Mono font
    kode_mono = tkFont.Font(family="kode mono", size=12)
    kode_mono_bold = tkFont.Font(family="kode mono", size=12, weight="bold")
    
    # Set the style
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' as a base theme
    style.configure("TFrame", background="#000000")
    style.configure("TLabel", background="#000000", foreground="white", font=kode_mono)
    style.configure("TScale", background="#000000", troughcolor="#333333", sliderlength=20)
    style.configure("TButton", background="#333333", foreground="white", font=kode_mono, padding=10, borderwidth=0)
    style.map("TButton", background=[('active', '#444444')])

    main_frame = ttk.Frame(root, padding=10, style="TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_label = ttk.Label(main_frame, text="MIKROFON LAUTSTÄRKE", style="TLabel")
    title_label.pack(pady=10)

    current_value = int(lines[0][8:10].strip())  # Extract current value from columns 9 and 10
    slider = ttk.Scale(main_frame, from_=-5, to=80, orient=tk.HORIZONTAL, length=300, command=lambda val: update_values(int(float(val))), style="TScale")
    slider.set(current_value)
    slider.pack(pady=10)

    value_label = ttk.Label(main_frame, text=f"AKTUELLE LAUTSTÄRKE: {current_value} DB", style="TLabel")
    value_label.pack(pady=10)

    link_frame = ttk.Frame(main_frame, style="TFrame")
    link_frame.pack(pady=10)

    made_by_label = ttk.Label(link_frame, text="MADE BY ", style="TLabel")
    made_by_label.pack(side=tk.LEFT)

    trfx_label = tk.Label(link_frame, text="TRFX", fg="white", cursor="hand2", bg="#000000", font=kode_mono_bold)
    trfx_label.pack(side=tk.LEFT)
    trfx_label.bind("<Button-1>", open_link)

    root.configure(bg="#000000")  # Set the background of the root window
    root.geometry("400x200")
    root.minsize(370, 230)  # Set the minimum size of the root window

    root.mainloop()
