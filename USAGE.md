# คู่มือการใช้งาน Exam Bank System

## วิธีการดาวน์โหลดระบบ

### วิธีที่ 1: ดาวน์โหลดเป็นไฟล์ ZIP (แนะนำสำหรับผู้ใช้ทั่วไป)

1. เปิดเว็บเบราว์เซอร์ไปที่ https://github.com/kornxi/exambank-system
2. คลิกปุ่ม **"Code"** สีเขียวที่มุมขวาบน
3. เลือก **"Download ZIP"**
4. รอให้ไฟล์ดาวน์โหลดเสร็จ
5. แตกไฟล์ ZIP ที่ดาวน์โหลดมา
6. เปิด Command Prompt หรือ Terminal
7. เข้าไปในโฟลเดอร์ที่แตกไฟล์:
   ```bash
   cd exambank-system-main
   ```

### วิธีที่ 2: Clone ด้วย Git (สำหรับนักพัฒนา)

```bash
git clone https://github.com/kornxi/exambank-system.git
cd exambank-system
```

## การติดตั้งและรันโปรแกรม

### 1. ติดตั้ง Python
- ต้องมี Python 3.7 หรือสูงกว่า
- ดาวน์โหลดได้จาก https://www.python.org/downloads/

### 2. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 3. รันโปรแกรม
```bash
python app.py
```

## ตัวอย่างการใช้งาน

### โหมดแบบโต้ตอบ (Interactive Mode)
```bash
python app.py
```

จะแสดงเมนู:
```
==================================================
ระบบธนาคารข้อสอบ (Exam Bank System)
==================================================
1. เพิ่มคำถามใหม่ (Add Question)
2. แสดงคำถามทั้งหมด (List All Questions)
3. ค้นหาคำถาม (Search Questions)
4. สร้างชุดข้อสอบ (Create Exam)
5. แสดงชุดข้อสอบ (List Exams)
6. ดูรายละเอียดชุดข้อสอบ (View Exam Details)
7. ลบคำถาม (Delete Question)
0. ออกจากระบบ (Exit)
==================================================
```

### โหมด Command Line
```bash
# ดูคำถามทั้งหมด
python app.py list

# ค้นหาคำถาม
python app.py search "Python"
```

## โครงสร้างโปรเจค

```
exambank-system/
├── README.md              # เอกสารหลัก
├── USAGE.md              # คู่มือนี้
├── LICENSE               # ใบอนุญาต
├── requirements.txt      # Python dependencies
├── setup.py             # ไฟล์ติดตั้ง
├── app.py               # แอปพลิเคชันหลัก
├── exambank/            # โมดูลหลัก
│   ├── __init__.py
│   ├── storage.py       # จัดการฐานข้อมูล
│   ├── question.py      # จัดการคำถาม
│   └── exam.py         # จัดการชุดข้อสอบ
├── data/               # ข้อมูล
│   ├── questions.json  # ธนาคารคำถาม
│   └── exams.json     # ชุดข้อสอบ
└── tests/             # ไฟล์ทดสอบ
    ├── __init__.py
    ├── test_storage.py
    └── test_question.py
```

## การทดสอบระบบ

```bash
python -m pytest tests/ -v
```

## การแก้ไขปัญหาที่พบบ่อย

### ปัญหา: ModuleNotFoundError
**วิธีแก้**: ติดตั้ง dependencies
```bash
pip install -r requirements.txt
```

### ปัญหา: ไม่สามารถสร้างไฟล์ data ได้
**วิธีแก้**: ตรวจสอบสิทธิ์การเขียนไฟล์ในโฟลเดอร์

### ปัญหา: Python ไม่รู้จักคำสั่ง
**วิธีแก้**: ติดตั้ง Python และเพิ่ม Python เข้า PATH

## ติดต่อและสนับสนุน

- GitHub: https://github.com/kornxi/exambank-system
- Issues: https://github.com/kornxi/exambank-system/issues

## License

MIT License - ใช้งานและแก้ไขได้ตามต้องการ
