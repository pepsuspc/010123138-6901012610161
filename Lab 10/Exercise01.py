import tkinter as tk

window = tk.Tk()
window.title("Counter App")
window.geometry("500x500")

count = 0

frame = tk.Frame(window,bg="lightblue",width=300,height=200,bd=3,relief=tk.RIDGE)
frame.pack(pady=20)

label = tk.Label(frame,text=int(count),font=("Arial",40),bg="lightblue")
label.pack(padx=20,pady=20)

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

frame1 = tk.Frame(window)
frame1.pack()

tk.Button(frame1, text="Increase",command=increase).pack(side="left",padx=5)
tk.Button(frame1, text="Decrease",command=decrease).pack(side="left",padx=5)
tk.Button(frame1, text="Reset",command=reset).pack(side="left",padx=5)
window.mainloop()