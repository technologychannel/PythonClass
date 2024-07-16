from product import Product

option_text = """
What do you want to do[1-2]?
1. Add Product
2. View All Product
"""
option = int(input(option_text))
if option == 1:
    p = Product(id=0,name= "", qty=0, price=0)
    p.id = int(input(f"Enter product id: "))
    p.name = input(f"Enter product name: ")
    p.qty = int(input(f"Enter product qty: "))
    p.price = float(input(f"Enter product price: "))
    f = open('products.csv','a')
    f.write(f"{p.id},{p.name},{p.qty},{p.price}\n")
    f.close()
    print("Product Added Scuccessfully")
elif option == 2:
    f = open("products.csv",'r')
    print("All Products are: \n------------------")
    print(f.read())
    print("------------------")
    
# Create a software for bank
# Customer[id, name, phone, balance]
# Create option to add and view customer