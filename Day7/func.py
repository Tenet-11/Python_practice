
# func.py
# Day7 文字分析工具：功能模組
# - 這個檔案只放「功能函式」
# - main.py 只負責流程與輸出

def clean_text(s, ignore_case=True, remove_punct=True):
    """清理文字：可選忽略大小寫、去標點、去前後空白"""
    s = s.strip()
    if ignore_case:
        s = s.lower()
    if remove_punct:
        for ch in ",.!?;:":
            s = s.replace(ch, "")
    return s


def counting(s):
    return len(s)

def vocabulary_num(s):
    s=clean_text(s)
    return len(s.split())
   
# 給定字串判斷單字出現頻率   
def voc_counting(s):
    s=clean_text(s)
    words=s.split()

    result={}
    for word in words:
        if word in result:
            result[word]+=1
        else:
            result[word]=1
    return result


def freq_max(s):
    max_count=0
    max_voc=""
    result=voc_counting(s)
    for word,count in result.items():
        if count>max_count:
            max_count=count
            max_voc=word
    
    return max_voc

def voc_list(s):
    # 進階: 依出現頻率排列(應用到lambda)
    result=voc_counting(s)
    sorted_list=sorted(result.items(),key=lambda x:x[1],reverse=True)
    return sorted_list