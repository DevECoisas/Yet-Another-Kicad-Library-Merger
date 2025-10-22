import os
import sys
from tkinter import *
from tkinter import ttk, filedialog, messagebox

# CLI arguments
try: directory = sys.argv[1]
except: directory = "./"
try: target_file_name = sys.argv[2]
except: target_file_name = "output"
try: target_directory = sys.argv[3]
except: target_directory = directory

# Merge function
def MergeLibraries(dir_path, target_filename, target_dir):
    paths = [p for p in os.listdir(dir_path)
             if p.endswith(".kicad_sym") and not p.endswith(target_filename + ".kicad_sym")]

    libs_treated = []
    for path in paths:
        with open(os.path.join(dir_path, path)) as lib:
            lines = lib.read().splitlines()
            content = [l for l in lines if "kicad_symbol_lib" not in l][:-1]
            libs_treated.append("\n".join(content))

    final_text = "(kicad_symbol_lib (version 20211014) (generator YAKLM,_made_by_DevECoisas)"
    for lib in libs_treated:
        final_text += "\n" + lib + "\n"
    final_text += ")"

    with open(os.path.join(target_dir, target_filename + ".kicad_sym"), "w") as f:
        f.write(final_text)

# GUI
root = Tk()
root.title("Yet Another KiCad Library Merger")
root.geometry("640x450")
root.config(bg="#1e1e24")

# Variables
input_dir = StringVar(value=os.getcwd())
output_name = StringVar(value="output")
output_dir = StringVar(value=os.getcwd())

# Functions
def select_input_dir():
    folder = filedialog.askdirectory()
    if folder:
        input_dir.set(folder)

def select_output_dir():
    folder = filedialog.askdirectory()
    if folder:
        output_dir.set(folder)

def merge_action():
    if not input_dir.get() or not output_name.get() or not output_dir.get():
        messagebox.showwarning("Incomplete", "Please fill all fields!")
        return
    MergeLibraries(input_dir.get(), output_name.get(), output_dir.get())
    messagebox.showinfo("Done", "Libraries merged successfully!")

# Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#eaa4a8", foreground="#000")
style.configure("TEntry", fieldbackground="#2afc98", foreground="#000")
style.configure("TButton", background="#00cfc1", foreground="#000", font=("Arial", 12))
style.map("TButton", background=[("active", "#00a398")], foreground=[("active", "#000")])

# Widgets
ttk.Label(root, text="Input Directory:").place(x=20, y=20, width=250, height=25)
ttk.Entry(root, textvariable=input_dir).place(x=20, y=50, width=500, height=25)
ttk.Button(root, text="Select Input Folder", command=select_input_dir).place(x=20, y=80, width=200, height=30)

ttk.Label(root, text="Output File Name:").place(x=20, y=130, width=250, height=25)
ttk.Entry(root, textvariable=output_name).place(x=20, y=160, width=500, height=25)

ttk.Label(root, text="Output Directory:").place(x=20, y=210, width=250, height=25)
ttk.Entry(root, textvariable=output_dir).place(x=20, y=240, width=500, height=25)
ttk.Button(root, text="Select Output Folder", command=select_output_dir).place(x=20, y=270, width=200, height=30)

ttk.Button(root, text="MERGE LIBRARIES", command=merge_action).place(x=220, y=350, width=200, height=50)

root.mainloop()
