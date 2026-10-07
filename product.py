   

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price =price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)

p1 = Product("Laptop", 1000)
p2 = Product("Zapatos", 100)

p1.apply_discount(10)
p2.apply_discount(20)

print(p1.name, "precio final:", p1.price)
print(p2.name, "precio final:", p2.price)

