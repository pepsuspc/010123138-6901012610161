import tkinter as tk

window = tk.Tk()
window.title("GUI Text Analyzer")
window.geometry("400x350")

tk.Label(window, text="ข้อความ").pack(pady=(10,0))
text_entry = tk.Entry(window,width=30)
text_entry.pack()

tk.Label(window, text="ตัวอักษรที่ต้องการนับ").pack(pady=(10, 0))
char_entry = tk.Entry(window, width=5)
char_entry.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

def count_character():
    text = text_entry.get()
    char = char_entry.get()
    if char == "":
        result_label.config(text="กรุณากรอกตัวอักษรที่ต้องการนับ")
        return
    count = text.lower().count(char.lower())
    result_label.config(text=f"ตัวอักษร '{char}' มี {count} ตัว")

def count_vowels():
    text = text_entry.get().lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    result_label.config(text=f"มีสระทั้งหมด {count} ตัว")

def check_palindrome():
    text = text_entry.get().lower().replace(" ", "")
    if text == "":
        result_label.config(text="กรุณากรอกข้อความ")
    elif text == text[::-1]:
        result_label.config(text="เป็น Palindrome")
    else:
        result_label.config(text="ไม่เป็น Palindrome")

tk.Button(window, text="Count Character", command=count_character).pack(pady=3)
tk.Button(window, text="Count Vowels", command=count_vowels).pack(pady=3)
tk.Button(window, text="Check Palindrome", command=check_palindrome).pack(pady=3)

window.mainloop()