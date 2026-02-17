# 📅 Day 2 — Python 容器（Containers）與資料結構基礎

---

## 🎯 學習目標

Day 2 的核心目標是深入理解 Python 四大容器的設計理念與底層邏輯，而不只是會使用語法。

1. 清楚區分以下四種容器：
   - list
   - tuple
   - dict
   - set

2. 理解並說明：
   - mutable 與 immutable 的差異
   - dynamic array 與 hash table 的概念
   - 常見操作的時間複雜度
   - 為什麼 dict / set 查找平均為 O(1)

3. 能回答以下問題：
   - 為什麼 list 不能當 dict 的 key？
   - 為什麼 tuple 可以當 dict 的 key？
   - list slicing 會不會產生新物件？

4. 能使用正確的容器解決問題，而非隨意選擇資料結構。

---

# 📘 學習內容

---

## 1️⃣ List

### 核心概念

- 有順序（ordered）
- 可重複元素
- 可修改（mutable）
- 底層為 Dynamic Array

### 特性理解

- 尾端新增元素平均時間複雜度為 O(1)
- 中間插入或刪除為 O(n)
- 成員查找為 O(n)
- slicing 會產生新 list（淺複製）


## 2️⃣ Tuple

### 核心概念

- 有順序
- 可重複
- 不可修改（immutable）

### 特性理解

- 因為不可變，因此可以被 hash
- 可作為 dict 的 key（若元素可 hash）
- 較 list 節省記憶體
- 適合表示固定結構資料

---

## 3️⃣ Dict（字典）

### 核心概念

- Key-Value 結構
- 底層為 Hash Table

### 特性理解

- Key 必須可 hash
- Key 不可重複
- Python 3.7+ 保留插入順序
- 查找效率高於 list

### 使用時機

- 需要快速查找
- 統計次數
- 建立映射關係

---

## 4️⃣ Set（集合）

### 核心概念

- 無順序
- 不可重複
- 底層為 Hash Table

### 特性理解

- 成員查找平均 O(1)
- 自動去重
- 適合做集合運算（聯集、交集、差集）

### 使用時機

- 去除重複
- 判斷成員是否存在
- 集合運算需求

---

# 🧠 核心理解整理

## Mutable vs Immutable

| 類型 | 意思 |
|------|------|
| **mutable** | 可以「改內容」 |
| **immutable** | 不能改內容，只能產生新物件 |

Mutable：
- list
- dict
- set

Immutable：
- tuple
- int
- str

---

##  Hash 與 Hash Table）
[Hash (雜湊)](https://ithelp.ithome.com.tw/articles/10208884)

### 一、什麼是 Hash？

Hash 是一個函式（hash function）。

它的功能是：
> 將任意大小的資料，轉換成固定大小的整數值。

### 二、為什麼需要 Hash？

如果不用 hash，要查找資料：

- 只能線性搜尋
- 時間複雜度 O(n)

使用 hash：

- 先將 key 經過 hash function
- 用 hash 結果定位位置
- 直接存取

平均時間複雜度降為：

O(1)

---

### 三、什麼是 Hash Table？

Hash Table 是一種資料結構。

本質是：

> Array + Hash Function

基本流程：

#### 插入

1. 計算 hash(key)
2. 將 hash 映射到陣列索引（通常用取餘數）
3. 存入該位置

#### 查找

1. 計算 hash(key)
2. 找到對應 index
3. 取出資料

## 為什麼 list 不能當 dict key？

因為 list 是 mutable，
mutable 物件的 hash 值可能改變，
因此不能作為 key。

---

## slicing 會產生新物件嗎？

會產生新的 list（淺複製）。

---

## 🧪 作業 1 — 單字出現次數統計

### 題目說明

輸入一串由空格分隔的單字，
統計每個單字出現的次數。

### 限制條件

- 必須使用 dict
- 不可使用 collections.Counter
- 必須自行實作統計邏輯

---

## 🧪 作業 2 — 集合運算

給定兩個 list：

1. 將其轉為 set
2. 輸出：
   - 聯集
   - 交集
   - 差集（a - b）

---

## 🧪 作業 3 — 思考題

1. 為什麼 dict 查找平均為 O(1)？
2. 為什麼 tuple 可以當 dict key，但 list 不行？
3. list slicing 是否會產生新物件？
4. 以下操作的時間複雜度為何？
   - list append
   - list 插入 index 0
   - dict 查找
   - set 成員查找

---

# 🚀 本日預期成果

完成 Day 2 後，我應該：

- 能清楚區分四大容器
- 理解底層結構與時間複雜度
- 能有意識地選擇適合的資料結構
- 用工程思維思考容器行為
