# 🎯 Face Attendance System

一個基於 AI 人臉辨識的打卡系統，結合 Webcam、Flask、PostgreSQL，實現完整的 Web 打卡流程。

本專案展示如何將 Computer Vision 技術整合進 Web 應用，打造一個可實際運作的打卡系統。

---

# 🚀 Demo 功能

- 📸 Webcam 即時打卡
- 🧠 人臉辨識（face_recognition）
- 🗄 打卡紀錄儲存（PostgreSQL）
- 📋 打卡紀錄查詢頁面
- 🔒 防止 60 秒內重複打卡

---

# 🧠 系統架構

```text
Browser (Webcam)
↓
Flask API (/checkin)
↓
Face Recognition
↓
PostgreSQL
↓
回傳結果
```

---

# 📂 專案結構

```
face-attendance-system/
├── app/
│ ├── main.py # Flask server
│ ├── attendance.py # 人臉辨識邏輯
│ ├── db.py # DB 操作
│ ├── templates/
│ │ ├── index.html # 打卡頁面
│ │ └── logs.html # 打卡紀錄頁
│ └── static/
│ └── js/
│ └── webcam.js # 前端攝影機控制
│
├── dataset/ # 人臉資料（不建議上傳）
├── encode_faces.py # 人臉 encoding
├── requirements.txt
└── README.md
```

---

# ⚙️ 技術堆疊

| 元件 | 技術 |
|------|------|
| Backend | Flask |
| AI | face_recognition (dlib) |
| Database | PostgreSQL |
| Frontend | HTML + JS |
| Camera | Web API (getUserMedia) |

---

# 🛠 安裝與執行
```bash
1️⃣ 建立虛擬環境
python3 -m venv venv
source venv/bin/activate
2️⃣ 安裝套件
pip install -r requirements.txt
3️⃣ 設定 PostgreSQL

建立資料庫：

CREATE DATABASE face_attendance;

建立資料表：

CREATE TABLE attendance_logs (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    checkin_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
4️⃣ 設定 DB 連線

修改：

app/db.py
conn = psycopg2.connect(
    dbname="face_attendance",
    user="postgres",
    password="你的密碼",
    host="localhost",
    port="5432"
)
5️⃣ 準備人臉資料

將圖片放入：

dataset/

例如：

dataset/
└── vance.jpg
6️⃣ 啟動系統
cd app
python main.py

打開瀏覽器：

http://127.0.0.1:5000
```

# 🧪 使用方式
# 📸 打卡

點擊：
📸 打卡

流程：
Webcam 拍照  
後端辨識人臉  
成功 → 寫入 PostgreSQL

# 📋 查看打卡紀錄

點擊：  
📋 查看打卡紀錄  
或直接訪問：  
/logs

# 🔒 防重複打卡機制

系統會檢查：  
同一個人 60 秒內只能打卡一次  
若重複打卡：  
⚠️ 請勿重複打卡

# 🧩 設計重點

使用 Flask 作為 Web API  
使用 face_recognition 做人臉比對  
使用 PostgreSQL 持久化資料  
前後端透過 fetch API 溝通  
加入 business logic（防重複打卡）

# 📊 專案價值

此專案展示：  
AI + Web + Database 整合能力  
REST API 設計  
前後端互動流程  
實務系統設計思維

# 🔮 未來可升級方向

👤 員工註冊（上傳人臉） 
🐳 Docker 部署  
☁️ 雲端部署（AWS / GCP）  
📊 打卡統計 dashboard  
🔐 登入驗證系統  
🎯 更準確的模型（InsightFace / ArcFace

# ⚠️ 注意事項

dataset 不建議上傳到 GitHub  
本專案為 Demo，未處理安全與高併發  
Webcam 需使用 HTTPS（正式環境）

# ✨ 作者
Vance