
# 去重並保留順序（Unique Words with Order）

text=input("請輸入一串單字: ")
words=text.split()

seen=set()
result=[]

for w in words:
    if w not in seen:
        seen.add(w)
        result.append(w)

# 用「空格」把 list 裡的字串接起來
print(" ".join(result))