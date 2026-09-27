class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def show_data(self):
        return f'Product Name = {self.name}\nPrice = {self.price}\nQuantity = {self.quantity}\n{"-" * 20}'

Arduino = Product("Arduino", 500, 3)
ESP32 = Product("ESP32", 250, 5)

print(Arduino.show_data())
print(ESP32.show_data())