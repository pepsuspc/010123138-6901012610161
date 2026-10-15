# w12 : Python (text mode)
# inheritance : Person -> Student, Employee
# method override + call superclass method, polymorphism

class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight  # kg
        self.height = height  # m

    def show_info(self):
        print("Name:", self.name)

    def get_BMI(self):
        return self.weight / (self.height * self.height)

class Student(Person):
    def __init__(self, name, weight, height, student_id):
        super().__init__(name, weight, height)
        self.student_id = student_id

    def show_info(self):  # override
        super().show_info()  # call superclass method
        print("Student ID:", self.student_id)

class Employee(Person):
    def __init__(self, name, weight, height, salary):
        super().__init__(name, weight, height)
        self.salary = salary

    def show_info(self):  # override
        super().show_info()
        print("Salary:", self.salary)

people = [Student("Alice", 50, 1.60, "S001"),
          Employee("Bob", 70, 1.75, 30000)]

i = 0
while i < len(people):
    people[i].show_info()  # same method name, different behaviour
    print("BMI:", round(people[i].get_BMI(), 2))
    print()
    i = i + 1
