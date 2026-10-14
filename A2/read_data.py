import json
import tkinter as tk

window = tk.Tk()
window.title("Borrow System")
window.geometry("1000x720")

listlabel = tk.Label(window,text="")
listlabel.pack()
listlabel_ = tk.Label(window,text="")
listlabel_.pack()

entrytoolsname = tk.Entry(window)
entrytoolsname.pack()
findtoolscode = tk.Label(window,text = "หารหัสอุปกรณ์")
findtoolscode.pack()

toolsframe = tk.Frame(window)

toolsdata = []

class tools:
    def __init__(self,code,name,status):
        self.code = code
        self.name = name 
        self.status = status
    def show_data(self):
        return f'Code = {self.code}\nName = {self.name}\nStatus = {self.status}'

def print_tools():
    toolsdata.clear()
    for widget in toolsframe.winfo_children():
        widget.destroy()

    with open("data.json","r",encoding="utf-8") as base:
        data = json.load(base)
    for item in data["tools"]:
        tool = tools(item["code"],item["name"],item["status"])
        toolsdata.append(tool)

    cards = []
    for row in toolsdata:
        card = tk.Label(toolsframe,text=row.show_data(),justify="left",anchor="w",relief="raised",borderwidth=1,width=22,padx=8,pady=8)
        cards.append(card)
    if len(cards) == 0:
        return 

    window.update_idletasks()
    card_width = cards[0].winfo_reqwidth() + 10
    columns = window.winfo_width() // card_width
    if columns < 1:
        columns = 1

    for i in range(len(cards)):
        cards[i].grid(row=i // columns, column=i % columns, padx=5, pady=5)


    
tk.Button(window,text="แสดงอุปกรณ์",command=print_tools).pack()
toolsframe.pack(pady=10)

window.mainloop()