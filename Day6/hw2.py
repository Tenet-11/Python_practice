# 作業 2：模擬 CSV 解析
line = "李晨綱, 20, New Taipei City"
name,age,city=[
    x.strip()
    for x in line.split(",")
]

print(f"name:{name}")
print(f"age:{age}")
print(f"city:{city}")

