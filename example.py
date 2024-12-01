import ttkbootstrap as ttk

# Setup TtkBootstrap
root = ttk.Window(themename="cosmo")

# Buat tombol dengan gaya sudut tumpul
button = ttk.Button(root, text="Click Me", style="success.TButton", command=lambda: print("Button clicked!"))
button.pack(pady=20)

root.mainloop()