import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("KALKULATOR")
window.geometry("300x400")
window.resizable(False,False)
window.configure(bg="white")
window.iconbitmap("./assets/calculator.ico")

characterInput=tk.StringVar()

frame1 = tk.Frame(window)
frame1.pack(fill="x")
frame1.configure(bg="white")

display=ttk.Entry(window, justify=tk.RIGHT, font=("Arial",25), textvariable=characterInput, state="readonly")
display.pack(fill="x",padx=10, pady=10)

frame2 = tk.Frame(window)
frame2.pack(fill="x", padx=6, pady=6)
frame2.configure(bg="white")

buttons = [
            ("C",0,0),("+",0,1),("-",0,2),("/",0,3),
            ("1",1,0),("2",1,1),("3",1,2),("x",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("=",3,3),
            ("7",3,0),("8",3,1),("9",3,2),("Del",4,0),
            ("0",4,1),(".",4,2),("^",2,3)
]

def onClick(char):
    if char == "=":
        try:
            equal=characterInput.get().replace("x","*").replace("^","**")
            result=eval(equal)
            characterInput.set(result)
        except:
            characterInput.set("Error")
    elif char == "C":
        characterInput.set("")
    elif char == ".":
        comma_input=characterInput.get()
        if not comma_input or comma_input[-1] in "+-x/.":
            characterInput.set(comma_input)
        else:
            characterInput.set(comma_input + ".")
    elif char == "Del":
        delete_input=characterInput.get()
        characterInput.set(delete_input[:-1])
    else:
        current_input=characterInput.get()
        characterInput.set(current_input + char)

for (char, row, col) in buttons:
    frame2.columnconfigure(col, weight=2)
    frame2.rowconfigure(row, weight=2)
    if char == "=":
        button = ttk.Button(frame2, text=char, command=lambda c=char: onClick(c))
        button.grid(column=col, row=row, padx=4, pady=4, rowspan=2, sticky='nesw')
    else:
        button = ttk.Button(frame2, text=char,command=lambda c=char: onClick(c))
        button.grid(column=col, row=row, padx=4, pady=4, ipady=15,sticky='nesw')



window.mainloop()
