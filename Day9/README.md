# 🎯 學習目標

Day 9 的核心目標是深入理解 class 的層級概念與進階功能，  
建立完整的物件導向結構思維。

完成本日學習後，我應該能：

1. 理解 class variable 與 instance variable 的差異
2. 使用 @classmethod
3. 使用 @staticmethod
4. 理解 __str__ 與 __repr__ 的用途
5. 理解封裝（Encapsulation）概念
6. 理解物件與類別層級的差異

---

# 🧠 本日核心思維

- instance 屬於物件
- class 屬於類別本身
- method 其實只是函式，但綁定在 class 上
- class 是設計，instance 是實體

---

# 📘 學習內容

---

## 1️⃣ Instance Variable vs Class Variable

### Instance Variable

- 屬於物件
- 每個 instance 都可以不同
- 存在於物件內部

### Class Variable

- 屬於類別本身
- 所有 instance 共享
- 適合放共用資訊

學習目標：

- 理解存放位置不同
- 理解共享與獨立差異

---

## 2️⃣ @classmethod

### 概念

- 第一個參數是 cls（代表類別）
- 可操作 class variable
- 常用於替代建構方式

學習目標：

- 理解 cls 與 self 的差別
- 知道何時使用 classmethod

---

## 3️⃣ @staticmethod

### 概念

- 不需要 self
- 不需要 cls
- 只是邏輯上歸類在 class 裡

使用情境：

- 工具函式
- 與 class 有關但不操作 class 狀態

---

## 4️⃣ __str__ 與 __repr__

### __str__

- 給使用者看的
- 讓物件印出時更友善
- **他會在print(物件)時被呼叫**


### __repr__

- 給開發者看的
- 用於除錯

學習目標：

- 讓物件印出來不再是記憶體位址
- 提升可讀性

---

## 5️⃣ 封裝（Encapsulation）

核心概念：

- 不讓外部直接操作內部資料
- 使用方法控制修改行為
- 降低耦合

---

# 📝 Day 9 課程作業

---

## 🧪 作業 1 — 升級 Person 類別

請在 Day 8 的 Person 類別中：

- 新增 class variable（例如：population）
- 每建立一個人，自動增加人口數
- 實作一個 classmethod 顯示目前人口

---

## 🧪 作業 2 — 升級 BankAccount 類別

新增：

- class variable 記錄總帳戶數
- __str__ 方法讓物件印出資訊更清楚
- 設計一個 staticmethod 驗證金額是否合法

---

## 🧪 作業 3 — 設計一個簡單的 Product 類別

功能：

- 商品名稱
- 價格
- 庫存數量

要求：

- 使用 instance variable
- 使用 class variable 統計商品總數
- 實作 __str__ 方法
- 設計增加庫存與減少庫存方法

---

# 🧩 思考題

1. 為什麼 class variable 不應該存放物件專屬資料？
2. @classmethod 與 @staticmethod 的差別是什麼？
3. __repr__ 為什麼在除錯時很重要？
4. 封裝為什麼可以降低錯誤？

---

# 🚀 本日預期成果

完成 Day 9 後，我應該：

- 理解 class 與 instance 層級
- 能設計共享屬性
- 能改善物件輸出格式
- 能使用 classmethod 與 staticmethod
- 具備些許進階 OOP 能力