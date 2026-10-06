import json

toolsdata = []

class tools:
    def __init__(self,code,name,status):
        self.code = code
        self.name = name 
        self.status = status
    def show_data(self):
        return f'Code = {self.code}\nName = {self.name}\nStatus = {self.status}'

with open("data.json","r",encoding="utf-8") as base:
    data = json.load(base)
for item in data["tools"]:
    tool = tools(item["code"],item["name"],item["status"])
    toolsdata.append(tool)

for row in toolsdata:
    print(row.show_data())
    print("-" * 20)