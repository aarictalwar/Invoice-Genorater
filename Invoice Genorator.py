import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
from datetime import datetime

root = tk.Tk()
root.title("Speed Logistics Invoice Generator")
root.geometry("650x480")
root.config(bg="#f9e9e9")

# ---------------------------
# Fixed company logo
# ---------------------------
LOGO_PATH = "Speed Logistics.png"   # <-- Always use this logo file


# ---------------------------
# UI Layout
# ---------------------------

tk.Label(root, text="Company Name:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
company_entry = tk.Entry(root, width=40)
company_entry.insert(0, "Speed Logistics")
company_entry.pack(anchor="w", padx=10)

# Logo preview text (not loading image for simplicity)
tk.Label(root, text=f"Using Logo: {LOGO_PATH}", fg="blue").pack(anchor="w", padx=10, pady=4)


# Date + Billing To
frame_info = tk.Frame(root)
frame_info.pack(anchor="w", padx=10, pady=10)

tk.Label(frame_info, text="Date:").grid(row=0, column=0, sticky="w")
date_entry = tk.Entry(frame_info, width=15)
date_entry.grid(row=0, column=1)
date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))

tk.Label(frame_info, text="Billing To:").grid(row=0, column=2, padx=15, sticky="w")
billto_entry = tk.Entry(frame_info, width=25)
billto_entry.grid(row=0, column=3)


# ---------------------------
# Items Table
# ---------------------------
tk.Label(root, text="Items (Description | Qty | Rate)", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
items_frame = tk.Frame(root)
items_frame.pack(padx=10)

item_entries = []

def add_row():
    desc = tk.Entry(items_frame, width=40)
    qty = tk.Entry(items_frame, width=6)
    rate = tk.Entry(items_frame, width=10)
    
    row = len(item_entries)
    desc.grid(row=row, column=0, padx=4, pady=4)
    qty.grid(row=row, column=1, padx=4)
    rate.grid(row=row, column=2, padx=4)

    item_entries.append((desc, qty, rate))

# start with 5 rows
for _ in range(5):
    add_row()

# Button to add more rows
tk.Button(root, text="Add Row", command=add_row).pack(anchor="w", padx=10, pady=5)


# ---------------------------
# Total Calculation
# ---------------------------
total_var = tk.StringVar(value="0.00")

def calculate_total():
    total = 0.0
    for desc, qty_entry, rate_entry in item_entries:
        q = qty_entry.get().strip()
        r = rate_entry.get().strip()
        if not q and not r:
            continue
        try:
            q = float(q or 0)
            r = float(r or 0)
        except:
            messagebox.showerror("Error", "Qty and Rate must be numbers.")
            return
        total += q * r

    total_var.set(f"{total:.2f}")

frame_total = tk.Frame(root)
frame_total.pack(anchor="e", padx=10, pady=10)

tk.Button(frame_total, text="Calculate Total", command=calculate_total).pack(side="left", padx=5)
tk.Label(frame_total, text="Total:", font=("Arial", 12, "bold")).pack(side="left")
