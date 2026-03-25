#step -1 import tkinter to use it 
import tkinter as tk
#step-2 GUI interaction 
root = tk.Tk()
root.geometry("320x450")
root.title("Smart calculator")
root.configure(bg="#1e1e1e")
#Adding inputs to our calculator
entry = tk.Entry(root, font=("Arial", 24), bg="#2d2d2d", fg="white",borderwidth=0, justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Instead of messy +,-,* we use this logic to perform calculations 
def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



#BUTTONS
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        if val == "=":
            cmd = calculate
        else:
            cmd = lambda v=val: press(v)

        tk.Button(frame, text=val, font=("Arial", 16),
                  bg="#333", fg="white", borderwidth=0,
                  width=5, height=2,
                  command=cmd).grid(row=r, column=c, padx=5, pady=5)

tk.Button(root, text="C", font=("Arial", 16),
          bg="#ff4d4d", fg="white",
          command=clear).pack(fill="both", padx=10, pady=5)

#Adding keyboard input(Additional feature from my end (not required))
def key_event(event):
    key = event.char

    if key in "0123456789+-*/.":
        press(key)
    elif key == "\r":  # Enter
        calculate()
    elif key == "\x08":  # Backspace
        entry.delete(len(entry.get())-1, tk.END)

root.bind("<Key>", key_event)

#Main loop
tk.mainloop()