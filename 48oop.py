class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price
    
    def display(self):
        print(f"Product name: {self.name}\tProduct Qty: {self.qty} \tProduct Price: {self.price}\n")


# Create object of product
p1 = Product(name="Samsung Galaxy M2", qty=10, price=25000)
p2 = Product(name="iPhone 15", qty=15, price=250000)
p3 = Product(name="Google Pixel 6", qty=8, price=60000)

p1.display()
p2.display()
p3.display()


