a = 5
print(type(a))

a = "hello"
print(type(a))

b=10
c=b
b=20
print(b)

ss=[1,2,3]
e=ss
ss.append(4)
print(e)

# 練習 3（理解記憶體）
f="hello"
print(id(f))
f+=" world"
print(id(f))

# ID變了，字串是 immutable

#   id 變了
#    = 記憶體位置變了
#    = 是新物件