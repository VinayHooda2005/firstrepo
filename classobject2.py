class Product:
    def __init__(self,name,price,quantity): 
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        return self.price * self.quantity


p1=Product("Pen",20,10)
p2=Product("Pencil",10,5)
p3=Product("eraser",5,10)
print("Name=",p1.name,"Price=",p1.price,"Quantity=",p1.quantity,"Total Price=",p1.total_price())
print("Name=",p2.name,"Price=",p2.price,"Quantity=",p2.quantity,"Total Price=",p2.total_price())
print("Name=",p3.name,"Price=",p3.price,"Quantity=",p3.quantity,"Total Price=",p3.total_price())