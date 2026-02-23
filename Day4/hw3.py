def mutate_demo(lst):
    lst.append("X")   # 原地修改
    lst = ["NEW"]     # 重新綁定（不影響外面）
    return lst

a = [1, 2, 3]
b = mutate_demo(a)

print("a =", a)  # a 會多一個 "X"
print("b =", b)  # b 是 ["NEW"]