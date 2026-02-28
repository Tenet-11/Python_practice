logs = [
    "INFO 2026-02-28 10:01:02 user=tom action=login",
    "ERROR 2026-02-28 10:01:05 user=tom msg=invalid_password",
    "WARN 2026-02-28 10:02:10 user=amy msg=slow_response",
    "ERROR 2026-02-28 10:03:22 user=amy msg=timeout",
    "INFO 2026-02-28 10:04:00 user=bob action=logout",
]

keyword="ERROR"
error_lines=[
    (i,line)
    for i,line in enumerate(logs)   # enumerate(集合)會產生(索引,元素)
    if keyword in line
]

count=len(error_lines)

print(f"關鍵字{keyword}出現次數{count}")
print(" ---- 相關行 (行號,內容) ---- ")
for i,line in error_lines:
    print(f"[{i}]: {line}")
