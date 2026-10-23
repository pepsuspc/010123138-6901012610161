import json
import tkinter as tk
from datetime import date, timedelta

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
selected_code = ""

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
        color = "#f6d0d0"
        if row.status == "ว่าง":
            color = "#d9f2d9"
        if row.code == selected_code:
            color = "#ffe08a"
            listlabel.config(text=f"เลือก : {row.code}  {row.name}  ({row.status})")

        card = tk.Button(toolsframe,text=row.show_data(),justify="left",anchor="w",relief="raised",borderwidth=1,width=22,padx=8,pady=8,
                         bg=color,command=lambda c=row.code: select_tool(c))
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


def load_data():
    with open("data.json","r",encoding="utf-8") as base:
        return json.load(base)

def save_data(data):
    with open("data.json","w",encoding="utf-8") as base:
        json.dump(data,base,ensure_ascii=False,indent=4)

def find_tool(data,code):
    for item in data["tools"]:
        if item["code"] == code:
            return item
    return None

def find_member(data,member_id):
    for item in data["members"]:
        if item["member_id"] == member_id:
            return item
    return None


def select_tool(code):
    global selected_code
    selected_code = code
    listlabel_.config(text="")
    print_tools()


def borrow_tool():
    if selected_code == "":
        listlabel_.config(text="กรุณาเลือกอุปกรณ์ก่อน",fg="red")
        return

    member_id = entrymember.get().strip()
    days_text = entrydays.get().strip()
    if not days_text.isdigit() or int(days_text) <= 0:
        listlabel_.config(text="จำนวนวันต้องเป็นตัวเลขที่มากกว่า 0",fg="red")
        return

    data = load_data()
    tool = find_tool(data,selected_code)
    member = find_member(data,member_id)

    if member is None:
        listlabel_.config(text=f"ไม่พบผู้ยืมรหัส {member_id}",fg="red")
        return
    if member["strike"] >= 3:
        listlabel_.config(text=f"{member['name']} ถูกระงับสิทธิ์ (คืนช้าครบ 3 ครั้ง)",fg="red")
        return
    if tool["status"] != "ว่าง":
        listlabel_.config(text=f"{tool['name']} ถูกยืมไปแล้ว",fg="red")
        return

    today = date.today()
    days = int(days_text)
    due = today + timedelta(days=days)

    new_loan = {
        "loan_id": f"L{len(data['loans']) + 1:03d}",
        "tool_code": tool["code"],
        "member_id": member_id,
        "loan_date": today.isoformat(),
        "duration": days,
        "due_date": due.isoformat(),
        "return_date": None,
    }
    data["loans"].append(new_loan)
    tool["status"] = "ถูกยืม"

    save_data(data)
    print_tools()
    listlabel_.config(text=f"{member['name']} ยืม {tool['name']} สำเร็จ  กำหนดคืน {due.isoformat()}",fg="green")


def return_tool():
    if selected_code == "":
        listlabel_.config(text="กรุณาเลือกอุปกรณ์ก่อน",fg="red")
        return

    data = load_data()

    loan = None
    for item in data["loans"]:
        if item["tool_code"] == selected_code and item["return_date"] is None:
            loan = item
    if loan is None:
        listlabel_.config(text="อุปกรณ์นี้ไม่ได้ถูกยืมอยู่",fg="red")
        return

    today = date.today()
    late = (today - date.fromisoformat(loan["due_date"])).days

    loan["return_date"] = today.isoformat()
    tool = find_tool(data,selected_code)
    tool["status"] = "ว่าง"

    message = f"คืน {tool['name']} ตรงเวลา ไม่มีค่าปรับ"
    if late > 0:
        member = find_member(data,loan["member_id"])
        member["strike"] = member["strike"] + 1
        message = f"คืน {tool['name']} ช้า {late} วัน ค่าปรับ {late * 10} บาท  |  {member['name']} ทำผิดสะสม {member['strike']}/3 ครั้ง"

    save_data(data)
    print_tools()
    listlabel_.config(text=message,fg="green")


tk.Button(window,text="แสดงอุปกรณ์",command=print_tools).pack()

controlframe = tk.Frame(window)
controlframe.pack(pady=5)
tk.Label(controlframe,text="รหัสผู้ยืม").grid(row=0,column=0,padx=5)
entrymember = tk.Entry(controlframe,width=18)
entrymember.grid(row=0,column=1,padx=5)
tk.Label(controlframe,text="จำนวนวัน").grid(row=0,column=2,padx=5)
entrydays = tk.Entry(controlframe,width=5)
entrydays.grid(row=0,column=3,padx=5)
tk.Button(controlframe,text="ยืม",width=8,command=borrow_tool).grid(row=0,column=4,padx=5)
tk.Button(controlframe,text="คืน",width=8,command=return_tool).grid(row=0,column=5,padx=5)

toolsframe.pack(pady=10)

window.mainloop()