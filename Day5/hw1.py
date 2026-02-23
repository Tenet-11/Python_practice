nums = [3, 7, 2, 8, 10, 5, 12]
new_nums=[]
thresold=50

for x in nums:
    if x%2==0:
        if x**2>thresold:
            new_nums=new_nums+[x**2]

print(new_nums)