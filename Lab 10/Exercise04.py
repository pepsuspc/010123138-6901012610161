import tkinter as tk

window = tk.Tk()
window.title("โจทย์เสริม")
window.geometry("400x350")

label = tk.Label(window, text="กรอกชื่อของคุณ")
label.pack(pady=20)
entry = tk.Entry(window)
entry.pack(pady=20)

def greeting():
    greet = str(entry.get())
    if greet == "" or greet == " ":
        label.config(fg="red",text="กรุณากรอกชื่อ")
    else:
        label.config(fg="black",text=f"สวัสดี , {greet}")

def clear():
    entry.delete(0,tk.END)

tk.Button(window,text="Greet",command=greeting).pack()
tk.Button(window,text="Clear",command=clear).pack()

window.mainloop()