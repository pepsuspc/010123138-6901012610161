class Vehicle():
    def __init__(self,license_plate,brand,model,year,daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
    def show_info(self):
        return f"License Plate : {self.license_plate}\nBrand : {self.brand}\nModel : {self.model}\nYear : {self.year}\nDaily Rate : {self.daily_rate}\n"

class Seat(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate,seat):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seat = seat
    def show_info(self):
        return super().show_info() + f"Seat : {self.seat}\n"

class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload
    def show_info(self):
        return super().show_info() + f"Payload : {self.payload} kg\n"

Ford = Truck("กง 7584","Ford Ranger","Raptor",2024, 3400, 1000)
print(Ford.show_info())