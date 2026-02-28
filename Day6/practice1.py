s="hello"
print("原本:",s,"id",id(s))

s=s+"!"
print("加上驚嘆號後:",s,"id",id(s))

# 不能直接改索引
try:
    s[0]="H"
except TypeError as e:
    print("不能改索引:",e)



# 常用字串方法
# lower/upper/strip/replace/find/count
text=" Hello, Python World    "

clean=text.strip()      # 去前後空白
lowered=text.lower()    # 小寫
uppered=text.upper()    # 大寫
replaced=clean.replace("Python","Data")  # 替換
pos=clean.find("World") # 找子字串位置(子字串起始位置)
cnt=clean.count("o")    # 統計字元/子字串出現次數

print("strip:",clean)
print("lower",lowered)
print("upper:",uppered)
print("replace:",replaced)
print("find(World):",pos)
print("count(o):",cnt)


# split 的用法
senetence="I  love  Python and    parsing"
words=senetence.split() #不給參數:自動用空白切，連續空白也會被處理掉
print(words)

csv_line="John, 25, Taipei"
parts=csv_line.split(",")
parts=[p.strip() for p in parts]
print(parts)


# join
# 把list組回字串(效率好的拼接)，和split是相反的操作
words_two=["apple","banana","orange"]
result=" | ".join(words_two)
print(result)

name="Junhui"
skills=["Python","Git","Parsing"]
profile=f"{name} skills:" + ", ".join(skills)
print(profile)

# 註解 f-string: 格式化輸出(含運算)
name="John"
age=25
city="Taipei"

print(f"姓名:{name}，年齡:{age}，城市:{city}")
print(f"明年年齡:{age+1}")
print(f"{name:>10} | {age:>3} | {city:<10}") #簡單對齊
