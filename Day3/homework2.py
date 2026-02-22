# 輸出前n項費式數列

n=int(input("請輸入要前幾項的費式數列: "))

a=0
b=1
for _ in range(n):
    print(a,end=" ")
    next_value=a+b
    a=b
    b=next_value
