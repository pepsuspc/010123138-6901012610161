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

toolsdata = []

class tools:
    def __init__(self,code,name,status):
        self.code = code
        self.name = name 
        self.status = status
    def show_data(self):
        return f'Code = {self.code}\nName = {self.name}\nStatus = {self.status}'

def print_tools():
    with open("data.json","r",encoding="utf-8") as base:
         data = json.load(base)
    for item in data["tools"]:
        tool = tools(item["code"],item["name"],item["status"])
        toolsdata.append(tool)
    for row in toolsdata:
        listlabel.config(text=f"{row.show_data()}")
        listlabel_.config(text=f"{"-" * 20}")


tk.Button(window,text="แสดงอุปกรณ์",command=print_tools).pack()


window.mainloop()