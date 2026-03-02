class Product:

    # class variable
    total_product=0
    all_products=[]

    # 建構子
    def __init__(self,name,price,stock):
        if not Product.is_valid_price(price):
            raise ValueError("Invalid price")
        
        if not Product.is_valid_amount(stock):
            raise ValueError("Invalid stock")

        self.name=name
        self.price=price
        self.stock=stock

        Product.total_product+=1
        Product.all_products.append(self)
    
    def add_stock(self,amount):
        self.stock+=amount
    
    def remove_stock(self,amount):
        if amount>self.stock:
            print("Not enough stock")
            return
        
        self.stock-=amount
    
    def apply_discount(self,percent):
        if not 0<percent<100:
            print("Invalid discount percentage")
        
        self.price*=(1-percent/100)

    
    # class method
    @classmethod
    def show_total_products(cls):
        print(f"Total products: {cls.total_product}")

    @classmethod
    def show_all_products(cls):
        for product in cls.all_products:
            print(product)
    

    # static method
    @staticmethod
    def is_valid_price(price):
        return isinstance(price,(int,float)) and price>=0
    
    @staticmethod
    def is_valid_amount(stock):
        return isinstance(stock,int) and stock>=0
    
    def __str__(self):
        return f"{self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"
    
    def __repr__(self):
        return f"Product(name={self.name},price={self.price},stock={self.stock})"
    


p1=Product("Keyboard",900,10)
p2=Product("Mouse",490,5)

print(p1)
print(p2)
print(repr(p1))

p1.add_stock(5)
p2.remove_stock(3)

p1.apply_discount(20)
print(p1)

Product.show_total_products()
Product.show_all_products()