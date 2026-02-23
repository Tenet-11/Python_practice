text = "  Python Is   VERY Powerful and Elegant  "
min_len = 5

words=[
    word
    for word in text.strip().lower().split()
    if len(word)>=min_len
]
print(words)