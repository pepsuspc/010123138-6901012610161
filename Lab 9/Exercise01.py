class Person():
    def __init__(self,Name,Address,Weight,Height):
        self.Name = Name
        self.Address = Address
        self.Weight = Weight
        self.Height = Height
    def show(self):
        return f"Name : {self.Name}\nAddress : {self.Address}\nWeight = {self.Weight}\nHeight = {self.Height}\n{"-" * 10}"
    def getBMI(self):
        return f"BMI = {self.Weight / (self.Height/100)**2}"

Guide = Person("Guide","KMUTT",55,168)
print(Guide.show())
print(Guide.getBMI())