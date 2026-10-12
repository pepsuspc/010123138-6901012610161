import tkinter as tk

window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")
window.geometry("350x250")

tk.Label(window, text="กรอกอุณหภูมิ (°C)").pack(pady=10)

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=20)

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        result_label.config(text=f"{fahrenheit:.2f} °F", fg="black")
    except ValueError:
        result_label.config(text="กรุณากรอกตัวเลขเท่านั้น", fg="red")

tk.Button(window, text="Convert", command=convert).pack()

window.mainloop()