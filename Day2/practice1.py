
#  list 

# 建立一個 list（直接給初始值）
a=[10,20,30]
print(a)


# 用 range 建立連續整數 list
# range(5) 代表 0 <= x < 5
# list(range(5)) 會轉成真正的 list
b=list(range(5))
print(b) # [0, 1, 2, 3, 4]


# 空list
cons=[]
for i in range(5):
    cons.append(i)
print(cons)  # [0, 1, 2, 3, 4]


#slicing
# 語法：list[start:end]
# 規則：start <= index < end
cons_slice=cons[1:4]
print("slice 1:4:",cons_slice)   # [1, 2, 3]

#反轉
# 語法：list[start:end:step]
# step = -1 代表從後往前走
# a[::-1] 會產生新的反轉 list
print("reverse: ",a[::-1])   # [30, 20, 10]



# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------

#  tuple
t=(10,20,30)
print(t)

# 只有一個元素的tuple要加逗號
single_t=(5,)
print(single_t)

# 存取元素 (用index)
print(t[0])
print(t[1])

# 長度
print("length: ",len(t))

# 查找(in 運算子)
print("20是否存在:",20 in t)

# tuple不可修改否則會報錯
# t[0] = 100   # ❌ TypeError


# tuple unpacking 
# 一次拆開多個值
aaa,bbb,ccc=t
print("unpacking:",aaa,bbb,ccc)


# tuple 裡面如果放 mutable 物件（例如 list）
# tuple 本身不能改，但裡面的 list 可以改
tuple_2=([1,2],[3,4])
tuple_2[0][0]=999
print(tuple_2)
# key:  tuple 不能改「元素指向」
#       但如果元素本身是 mutable，可以改它的內容




# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------

#  dict
#  dict 是「key → value」的對應表，用key找資料( 對應C++中的map)

# 建立dict
d={
    "name":"Jack",
    "age":20,
    "major":"CS"
}
print(d)

# 讀取資料(用key)
print(d["name"])
print(d["age"])

# 修改/新增資料
d["age"]=21
d["gpa"]=4.0

# 刪除資料
del d["major"]
print(d)

# 查找資料是否存在
print("name" in d)  #TRUE
print("height" in d) #FALSE

# 取得所有key/value
print(d.keys())
print(d.values())
print(d.items())  # 取得所有 (key, value) 配對

# 用for迴圈走訪
for key in d:
    print(key,d[key])
for key,value in d.items():
    print(key,value)
