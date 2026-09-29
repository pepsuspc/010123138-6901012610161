class Vehicle():
    def __init__(self,license_plate,brand,model,year,daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
    def show_info(self):
        return f"License Plate : {self.license_plate}\nBrand : {self.brand}\nModel : {self.model}\nYear : {self.year}\nDaily Rate : {self.daily_rate}\n"
    def calculate_rental_cost(self, days):
        return f"Paid : {days * self.daily_rate}"

class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate,seat):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seat = seat
    def show_info(self):
        return super().show_info() + f"Seat : {self.seat}"
    def calculate_rental_cost(self, days):
        if days == 5:
            return f"Paid : {days * self.daily_rate}\nCongrat You granted 2 days free for rented this car"
        elif days == 7:
            return f"Paid : {5 * self.daily_rate}\nCongrat You granted 2 days free for rented this car"
        return super().calculate_rental_cost(days)
    
class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload
    def show_info(self):
        return super().show_info() + f"Payload : {self.payload} kg"
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)

Ford = Truck("กง 7584","Ford Ranger","Raptor",2024, 3400, 1000)
print(Ford.show_info())
print(Ford.calculate_rental_cost(5))

Civic = Car("1กข 1234", "Honda", "Civic", 2023, 1500, 5)
print(Civic.show_info())
print(Civic.calculate_rental_cost(7))