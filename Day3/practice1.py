
# if
x=10
if x>0:
    print("正數")
elif x==0:
    print("零")
else:
    print("負數")


y=int(input()) # 因為input出來是字串
if y%2==0:
    print("偶數")
else:
    print("奇數")



# for
# Python 的 for 是：「把 iterable 裡的東西一個一個拿出來」
for i in range(5):
    print(i)

numbers=[10,20,30,40,50]
for n in numbers:
    print(n)

names=["Amy","Bob","Cindy"]
for index,name in enumerate(names):
    print(index,name)

# 使用zip同時遍歷多個序列
# zip 會跑：最短的那個序列長度
zip_name=["Amy","Bob","Cindy"]
zip_score=[85,92,78]
zip_age=[18,19,20]

for name,score,age in zip(zip_name,zip_score,zip_age):
    print(name,score,age)


# while
# 只要條件為 True 就一直跑
count=0
while count<5:
    print(count)
    count+=1

temp=10
while temp>0:
    print(temp)
    temp-=1


# break與continue

# note: range(start, stop, step)
# step是-1代表大到小

# 遇到5就停
for i in range(10):
    if i==5:
        break
    print(i)

# 跳過偶數
for i in range(10):
    if i%2==0:
        continue
    print(i)

for i in range(1,31):
    if i%5==0:
        continue
    if i==23:
        break
    print(i)

