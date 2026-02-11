# 問題: 輸入一串「空格分隔」的數字
# 輸出： 總和、最大值、最小值、平均數

s=input("請輸入數字: ")
parts=s.split()
numbers=[]
for p in parts:
    numbers.append(int(p))

# 計算總和
total=0
for num in numbers:
    total+=num
print(total)

# 計算最大值
max_value=numbers[0]
for num in numbers:
    if num>max_value:
        max_value=num
print(max_value)

# 計算最小值
min_value=numbers[0]
for num in numbers:
    if num<min_value:
        min_value=num
print(min_value)

#計算平均數
average=total/len(numbers)
print(average)