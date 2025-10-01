# Exam Bank System

ระบบธนาคารข้อสอบ (Exam Bank System) - A simple exam question bank management system

## คุณสมบัติ (Features)

- เพิ่ม แก้ไข และลบคำถามข้อสอบ (Add, edit, and delete exam questions)
- จัดหมวดหมู่คำถามตามวิชาและหัวข้อ (Categorize questions by subject and topic)
- สร้างชุดข้อสอบจากธนาคารคำถาม (Create exam sets from question bank)
- ค้นหาคำถามด้วยคำสำคัญ (Search questions by keywords)
- จัดเก็บข้อมูลในรูปแบบ JSON (Store data in JSON format)

## การติดตั้ง (Installation)

### วิธีที่ 1: ดาวน์โหลดเป็นไฟล์ ZIP (Download as ZIP)

1. ไปที่ https://github.com/kornxi/exambank-system
2. คลิกปุ่ม "Code" สีเขียว
3. เลือก "Download ZIP"
4. แตกไฟล์ ZIP ที่ดาวน์โหลดมา

### วิธีที่ 2: Clone จาก GitHub

```bash
git clone https://github.com/kornxi/exambank-system.git
cd exambank-system
```

### ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

## การใช้งาน (Usage)

### เริ่มต้นระบบ (Start the system)

```bash
python app.py
```

### ตัวอย่างการใช้งาน (Examples)

```python
# เพิ่มคำถามใหม่ (Add a new question)
python app.py add

# ดูคำถามทั้งหมด (View all questions)
python app.py list

# ค้นหาคำถาม (Search questions)
python app.py search "keyword"

# สร้างชุดข้อสอบ (Create exam set)
python app.py create-exam
```

## โครงสร้างโปรเจค (Project Structure)

```
exambank-system/
├── app.py                 # แอปพลิเคชันหลัก (Main application)
├── exambank/             # โมดูลหลักของระบบ (Core modules)
│   ├── __init__.py
│   ├── question.py       # จัดการคำถาม (Question management)
│   ├── exam.py          # จัดการชุดข้อสอบ (Exam management)
│   └── storage.py       # จัดการฐานข้อมูล (Database management)
├── data/                # ข้อมูลและไฟล์ JSON (Data and JSON files)
│   ├── questions.json   # ธนาคารคำถาม (Question bank)
│   └── exams.json      # ชุดข้อสอบ (Exam sets)
├── tests/              # ไฟล์ทดสอบ (Test files)
├── requirements.txt    # Python dependencies
├── README.md          # เอกสารนี้ (This document)
└── LICENSE            # ลิขสิทธิ์ (License)
```

## การพัฒนา (Development)

### รันการทดสอบ (Run tests)

```bash
python -m pytest tests/
```

## License

MIT License - ดูรายละเอียดใน LICENSE file

## ติดต่อ (Contact)

GitHub: [@kornxi](https://github.com/kornxi)
