# 計算機函式
def calc(a,b,op):
     if op == "+":
        return a + b
     elif op == "-":
        return a - b
     elif op == "*":
        return a * b
     elif op == "/":
        if b == 0:
            return "除數不能為 0"
        return a / b
     else:
        return "不支援的運算符號"
     

a,b=map(int,input("請輸入兩個數字: ").split())
print(calc(a, b, "+"))
print(calc(a, b, "-"))
print(calc(a, b, "*"))
print(calc(a, b, "/"))
print(calc(a, 0, "/"))