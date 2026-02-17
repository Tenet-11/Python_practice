
text=input("請輸入一串由空白分隔的單字: " )

# 把各個單字切割出來
words=text.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

for word in word_count:
    print(word,":",word_count[word])