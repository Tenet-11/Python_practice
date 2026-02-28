# 作業 1：單字過濾器

text="   Python is fun, and parsing is powerful!   "
min_len=5

clean=text.lower()
for ch in [",","!"]:
    clean=clean.replace(ch," ")
words=clean.split()

flitered=[
    w
    for w in words
    if len(w)>=min_len
]
print(flitered)
