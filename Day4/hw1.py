# 判斷質數
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    
    return True


# 費式數列
def Fibonacci(n):
    seq=[]
    a,b=0,1
    for _ in range(n):
        seq.append(a)
        next_value=a+b
        a=b
        b=next_value
    return seq

# 成績分級
def grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"




## 主程式
# --- Prime ---
n = int(input("請輸入整數判斷是否質數："))
print("是質數" if is_prime(n) else "不是質數")

# --- Fibonacci ---
k = int(input("請輸入費氏數列項數："))
print(Fibonacci(k))

# --- Grade ---
scores = [95, 82, 76, 61, 50]
for s in scores:
    print(f"成績 {s} → 等第 {grade(s)}")