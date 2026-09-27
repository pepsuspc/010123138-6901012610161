import json

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def show_data(self):
        return f'Product Name = {self.name}\nPrice = {self.price}\nQuantity = {self.quantity}\n{"-" * 20}'

with open("Exercise04_productdata.json","r",encoding="utf-8") as file:
    data = json.load(file)

Products = []
for item in data:
    product = Product(item["product_name"],item["price"],item["quantity"])
    Products.append(product)

for row in Products:
    print(row.show_data())
    print("-" * 20)

names = [row.name for row in Products]
prices = [row.price for row in Products]
quantities = [row.quantity for row in Products]

volumes = []
for i in range(len(prices)):
    volumes.append(prices[i] * quantities[i])

current_max = volumes[0]
for i in range(len(volumes)):
    if volumes[i] > current_max:
        current_max = volumes[i]

print(current_max)
