class Person:

    # ==============================
    # 🔹 Class Variables（全班共用）
    # ==============================
    species="Human"
    population=0


    # ==============================
    # 🔹 建構子（Instance 建立時執行）
    # ==============================
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.population+=1
    
    # ==============================
    # 1️⃣ Instance Method
    # ==============================
    def introduce(self):
        print(f"Hi, I am {self.name},{self.age} years old.")

    # ==============================
    # 2️⃣ Class Method
    # ==============================
    @classmethod
    def show_population(cls):
        print(f"Population: {cls.population}")

    @classmethod
    def reset_population(cls):
        cls.population=0
    
    # 替代建構子: 提供另一種「建立物件」的方式
    @classmethod
    def from_string(cls,s):
        name, age=s.split(",")
        return cls(name,int(age))
        # 等價於: Person.__init__(新物件, name, age)
    

    # ==============================
    # 3️⃣ Static Method
    # ==============================
    def is_valid_age(age):
        return isinstance(age,int) and age>=0 # 檢查「某個東西是不是某種型別」










Person.show_population()

p1=Person("Alex",20)
p2=Person("Brian",25)

print(p1.species)
print(p2.species)

Person.species="Homo sapiens"
print(p1.species)
print(p2.species)

# 牽扯到一個重要觀念
# Python可以在main裡面幫class動態新增屬性(但不推薦這樣做)
p1.species="Handsome"
print(p1.species)
print(p2.species)


Person.show_population()

p3=Person.from_string("Cindy,18")
Person.show_population()

Person.reset_population()
Person.show_population()

print(Person.is_valid_age(20)) #T
print(Person.is_valid_age(-5)) #F
print(Person.is_valid_age("hi")) #F