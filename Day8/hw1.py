class Person:

    def __init__(self,name,age):
        # Instance variable
        # 左邊是物件的屬性，右邊是傳進來的參數
        self.name=name
        self.age=age

    def introduce(self):
        if(self.age==1):
            print(f"Hi, I am {self.name}. I am 1 year old")
        else:
             print(f"Hi, I am {self.name}. I am {self.age} years old")
       

    def grow_older(self):
        self.age+=1
        print(f"{self.name} is now {self.age} years old.")


p1=Person("Alex",20)
p2=Person("Brian",25)

p1.introduce()
p2.introduce()

p1.grow_older()
p1.introduce()
p2.introduce()
