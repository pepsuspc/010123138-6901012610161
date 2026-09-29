class Vehicle():
    def __init__(self,license_plate,brand,model,year,daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
    def show_info(self):
        return f"License Plate : {self.license_plate}\nBrand : {self.brand}\nModel : {self.model}\nYear : {self.year}\nDaily Rate : {self.daily_rate}"

Mclaren = Vehicle("กง 7584","Mclaren","720s",2017, 187000)
print(Mclaren.show_info())