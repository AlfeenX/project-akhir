import tkinter as tk
from tkinter import ttk

class Kalkulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KALKULATOR")
        self.geometry("300x400")
        self.resizable(0,0)
        self.iconbitmap("./assets/calculator.ico")
        self.configure(bg="white")
        
        characterInput=tk.StringVar()
        
        self.frame1=tk.Frame( bg="white")
        self.frame1.pack(fill="x")
        
        display=ttk.Entry(self.frame1, font=("Arial", 25), justify=tk.RIGHT, state="readonly", textvariable=characterInput)
        display.pack(fill="x",padx=10,pady=10)
        
        self.frame2=tk.Frame( bg="white")
        self.frame2.pack(fill="x", padx=6)
        
        buttons=[
            ("C",0,0),("+",0,1),("-",0,2),("/",0,3),
            ("1",1,0),("2",1,1),("3",1,2),("x",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("=",3,3),
            ("7",3,0),("8",3,1),("9",3,2),("Del",4,0),
            ("0",4,1),(".",4,2),("^",2,3)
        ]
        
        for (char,row,col) in buttons:
            self.frame2.columnconfigure(row, weight=2)
            self.frame2.rowconfigure(col, weight=1)
            if char == "=":
                tombol=ttk.Button(self.frame2, text=char, command=lambda c=char: onClick(c))
                tombol.grid(column=col,row=row,ipady=15,rowspan=2,padx=4, pady=4, sticky="nesw",)
            else:
                tombol=ttk.Button(self.frame2, text=char, command=lambda c=char: onClick(c))
                tombol.grid(column=col,row=row,ipady=15,padx=4, pady=4, sticky="nesw")
        
        def onClick(char):
            if char == "C":
                characterInput.set("")
            elif char == "=":
                try:
                    expression=characterInput.get().replace("x","*").replace("^","**")
                    result=eval(expression)
                    characterInput.set(result)
                except Exception:
                    characterInput.set("Error")
                
            elif char == "Del":
                delete_input=characterInput.get()
                characterInput.set(delete_input[:-1])
            elif char== ",":
                comma_input=characterInput.get()
                if not comma_input or comma_input[-1] in "x+-/.":
                    characterInput.set(comma_input)
                else:
                    characterInput.set(comma_input + ".")
            else:
                current_input=characterInput.get()
                characterInput.set(current_input + char)
            
            
if __name__=="__main__":
    kalk=Kalkulator()
    kalk.mainloop()
                