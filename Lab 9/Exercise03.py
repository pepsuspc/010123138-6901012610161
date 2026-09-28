class Person():
    def __init__(self,Name,Address,Weight,Height):
        self.Name = Name
        self.Address = Address
        self.Weight = Weight
        self.Height = Height
    def show(self):
        return f"Name : {self.Name}\nAddress : {self.Address}\nWeight = {self.Weight}\nHeight = {self.Height}\n"
    def getBMI(self):
        return f"BMI = {(self.Weight / (self.Height/100)**2):.2f}\n{"-" * 20}"

class Student(Person):
    def __init__(self, Name, Address, Weight, Height, student_id, course, gpa):
        super().__init__(Name, Address, Weight, Height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa
    def show(self):
        return super().show() + f"StudentID = {self.student_id}\nCourse = {self.course}\nGPA = {self.gpa}"
    def getBMI(self):
        return super().getBMI()

class Employee(Person):
    def __init__(self, Name, Address, Weight, Height,employee_id,department,salary):
        super().__init__(Name, Address, Weight, Height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    def show(self):
        return super().show() + f"EmployeeID = {self.employee_id}\nDepartment = {self.department}\nSalary = {self.salary}"
    def getBMI(self):
        return super().getBMI()
            
Guide = Student("Guide","KMUTT",55,168,22400,"CMM",3.50)
Tawa = Employee("Tawa","BU",65,180,"007","Film",75000)

print(Guide.show())
print(Guide.getBMI())

print(Tawa.show())
print(Tawa.getBMI())