# main.py
# Day7 CLI 文字分析工具（主程式）
# 這個檔案負責：
# 1) 取得使用者輸入
# 2) 呼叫 func.py 裡的功能
# 3) 統一輸出結果（把「計算邏輯」留在 func.py）


import func

user_input=input("請輸入一段文字: ")

# 1) 基本統計
print("字元數:", func.counting(user_input))
print("單字數:", func.vocabulary_num(user_input))

# 2) 字頻統計
word_dict = func.voc_counting(user_input)
for word, count in word_dict.items():
    print(f"{word} 出現了 {count} 次")

# 3) 出現最多的單字
frequency_max = func.freq_max(user_input)
print(f"出現最多次的單字是 {frequency_max}")

# 4) 依頻率排序（回傳 list[tuple]）
print("依頻率排序:", func.voc_list(user_input))