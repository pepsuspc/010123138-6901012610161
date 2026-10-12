import tkinter as tk

window = tk.Tk()
window.title("Test Slide")
window.geometry("1000x1000")

label = tk.Label(window,text = "หมาอ้วน") #label ต้องมีการ pack
label.pack(pady=20)

entry = tk.Entry(window) #รับ input
entry.pack(pady=20)
entry1 = tk.Entry(window) #รับ input
entry1.pack(pady=20)

frame = tk.Frame(window, bg="lightblue",width=200,height=100,bd=3,relief=tk.RIDGE) #สร้างกรอบ
frame.pack(padx=20,pady=20)

label1 = tk.Label(frame,text = "หมาอ้วน",bg="lightblue") 
label1.pack(padx=20,pady=20)

# button = tk.Button(window,text="Multiply") #ปุ่มกด 
# button.pack()

#สร้างตัวรับ Event
def multiply():
    try:
        num1 = float(entry.get())
        num2 = float(entry1.get())
        result = num1 * num2
        label.config(text=result)
    except ValueError:
        label.config(text="Wrong type argument")

button = tk.Button(window,text="Multiply",command=multiply) #ปุ่มกด 
button.pack()

window.mainloop()
