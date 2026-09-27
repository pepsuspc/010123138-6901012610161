class Student:
    def __init__(self,student_id,name,course,age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age
    def show_data(self):
        return f'ID : {self.student_id}\nName : {self.name}\nCourse : {self.course}\nAge : {self.age}'

Auto = Student(22333,"Auto","IE",18)

print(Auto.show_data())