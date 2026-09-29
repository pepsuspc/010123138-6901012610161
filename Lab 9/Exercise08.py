class myBag():
    def __init__(self,Things):
        self.Things = list(Things)
    def show(self):
        return f"Things : {self.Things}"
    def add(self,Thing_added):
        self.Things.append(Thing_added)
    def remove(self,Things_remove):
        if Things_remove in self.Things:
            self.Things.remove(Things_remove)
        else:
            print(f"{Things_remove} is not in the bag")

mybag = myBag(["Laptop","Wallet","Mouse"])
print(mybag.show())
mybag.add("Phone")
print(mybag.show())
mybag.remove("Wallet")
print(mybag.show())