scores = [95, 82, 76, 61, 50]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # f-string
    # 把變數的值「插入」到字串裡面
    print(f"成績 {score} → 等第 {grade}")