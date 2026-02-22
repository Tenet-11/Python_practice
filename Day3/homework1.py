
# 給定一個數判斷是否質數
n=int(input("請輸入整數:"))

if n<=1:
    print("不是質數")
else:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    
    if is_prime:
        print("是質數")
    else:
        print("不是質數")