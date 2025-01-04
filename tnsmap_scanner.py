"""
This tool is designed to demonstrate network scanning and penetration testing techniques using nmap through proxychains and Tor.
The user is solely responsible for obtaining proper authorization before scanning any network or system. Unauthorized scanning is illegal and unethical.
Ensure compliance with all applicable local, state, national, and international laws before using this software
"""

import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

# Tool created by RDN
# This tool scans network targets using nmap via proxychains and Tor for anonymity.
# Educational use only. Unauthorized scanning is illegal and unethical.

process = None

ascii_art = r"""
┏┳┓┓   ┳┓•  ┓  ┏┓   ┓┓     
 ┃ ┣┓┏┓┃┃┓┏┓┣┓╋┗┓╋┏┓┃┃┏┏┓┏┓
 ┻ ┛┗┗ ┛┗┗┗┫┛┗┗┗┛┗┗┻┗┛┗┗ ┛                                     
"""

def is_tor_active():
    try:
        result = subprocess.run(["sudo", "service", "tor", "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if "active (exited)" in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        return False

def scan_target():
    global process
    target = entry_target.get()
    if not target:
        messagebox.showwarning("Input Error", "No target specified. Please enter an IP address or hostname.")
        return

    if not is_tor_active():
        messagebox.showerror("Service Error", "Proxychains or Tor service is not active. Please ensure they are running.")
        return

    output_text.delete(1.0, tk.END) 
    output_text.insert(tk.END, ascii_art) 
    output_text.insert(tk.END, f"Scanning {target} through proxychains...\n")

    process = threading.Thread(target=run_nmap, args=(target,))
    process.start()

def run_nmap(target):
    global process
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ascii_art) 
    output_text.insert(tk.END, f"Running Nmap with Proxychains on {target}...\n")

    try:
        command = f"proxychains4 nmap -sV -A -Pn {target}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            output_text.insert(tk.END, f"Error: {result.stderr}\n")
        else:
            output_text.insert(tk.END, result.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def cancel_scan():
    global process
    if process is not None:
        os.system("pkill -f 'nmap'") 
        output_text.insert(tk.END, "Scan canceled.\n")
        process = None

root = tk.Tk()
root.title("TNSMAP Scanner")

root.geometry("800x600") 

root.configure(bg='black')

label_target = tk.Label(root, text="Enter target IP address or hostname:", bg='black', fg='red', font=('Helvetica', 12))
label_target.pack(pady=10)

entry_target = tk.Entry(root, width=50, bg='gray', fg='white', font=('Helvetica', 12))
entry_target.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(frame, height=20, width=70, bg='black', fg='lime', font=('Courier New', 10), yscrollcommand=scrollbar.set)
output_text.pack(side=tk.LEFT)

scrollbar.config(command=output_text.yview)

run_nmap_button = tk.Button(root, text="Start Scanning", command=scan_target, bg='#cc0000', fg='black', font=('Courier New', 14, 'bold'), relief="raised", bd=3)
run_nmap_button.pack(pady=20)

cancel_button = tk.Button(root, text="Cancel Scan", command=cancel_scan, bg='#cc0000', fg='black', font=('Courier New', 14, 'bold'), relief="raised", bd=3)
cancel_button.pack(pady=10)

root.mainloop()