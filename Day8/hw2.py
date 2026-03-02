class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        
        if balance < 0:
            print("Initial balance cannot be negative. Set to 0.")
            self.balance = 0
        else:
            self.balance = balance

    def deposit(self, money):
        if money <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += money
            print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, money):
        if money <= 0:
            print("Withdrawal amount must be positive.")
        elif money > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= money
            print(f"Withdrawal successful. New balance: {self.balance}")

    def show(self):
        print(f"{self.name}'s account balance is {self.balance}")


p1=BankAccount("Jimmy",1000)
p2=BankAccount("Dylan",1000)
p3=BankAccount("Neil",1000000)

p1.deposit(1000)
p2.withdraw(500)
p1.show()
p2.show()
p3.show()