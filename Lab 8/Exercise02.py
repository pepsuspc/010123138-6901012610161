import json as j    

class Student:
    def __init__(self,student_id,name,course,age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age
    def show_data(self):
        return f'ID : {self.student_id}\nName : {self.name}\nCourse : {self.course}\nAge : {self.age}'

with open("Exercise02_studentdata.json","r",encoding="utf-8") as file:
    data = j.load(file)

Students = []
for item in data:
    student = Student(item["student_id"],item["name"],item["course"],item["age"])
    Students.append(student)

for j in Students:
    print(j.show_data())
    print("-" * 20)

ids = [j.student_id for j in Students]
names = [j.name for j in Students]
courses = [j.course for j in Students]
ages = [j.age for j in Students]

currentmin = ages[0]
for age in ages:
    if age < currentmin:
        currentmin = age
print(currentmin)