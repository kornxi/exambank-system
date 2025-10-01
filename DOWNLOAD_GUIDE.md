# 📥 คู่มือการดาวน์โหลดระบบ (Download Guide)

## วิธีการดาวน์โหลดไฟล์ทั้งหมดเป็น ZIP

### ขั้นตอนที่ 1: เข้าสู่หน้า GitHub Repository
🌐 เปิดเว็บเบราว์เซอร์แล้วไปที่:
```
https://github.com/kornxi/exambank-system
```

### ขั้นตอนที่ 2: หาปุ่ม "Code"
🟢 มองหาปุ่มสีเขียวที่เขียนว่า **"Code"** อยู่ทางขวาบน

ตำแหน่งของปุ่ม:
- อยู่ด้านขวาของหน้า
- เหนือรายการไฟล์
- ติดกับปุ่ม "Add file"

### ขั้นตอนที่ 3: คลิกปุ่ม "Code"
👆 คลิกที่ปุ่ม **"Code"** สีเขียว จะมีเมนูแสดงขึ้นมา

### ขั้นตอนที่ 4: เลือก "Download ZIP"
📦 ในเมนูที่แสดงขึ้นมา เลือกตัวเลือก **"Download ZIP"**

มันจะอยู่:
- ตอนล่างของเมนู
- มีไอคอนรูปลูกศรชี้ลง
- เขียนว่า "Download ZIP"

### ขั้นตอนที่ 5: รอการดาวน์โหลด
⏳ ไฟล์ชื่อ `exambank-system-main.zip` จะเริ่มดาวน์โหลด

ขนาดไฟล์: ประมาณ 50 KB

### ขั้นตอนที่ 6: แตกไฟล์ ZIP
📂 เมื่อดาวน์โหลดเสร็จแล้ว:

**บน Windows:**
1. คลิกขวาที่ไฟล์ ZIP
2. เลือก "Extract All..." หรือ "แตกไฟล์ทั้งหมด"
3. เลือกตำแหน่งที่ต้องการ
4. กด "Extract" หรือ "แตกไฟล์"

**บน macOS:**
1. ดับเบิลคลิกที่ไฟล์ ZIP
2. ไฟล์จะแตกอัตโนมัติ

**บน Linux:**
```bash
unzip exambank-system-main.zip
cd exambank-system-main
```

### ขั้นตอนที่ 7: เข้าสู่โฟลเดอร์
📁 เปิดโฟลเดอร์ `exambank-system-main` ที่แตกออกมา

คุณจะเห็นไฟล์:
```
exambank-system-main/
├── README.md
├── USAGE.md
├── EXAMPLES.md
├── SUMMARY.md
├── app.py
├── requirements.txt
├── setup.py
├── LICENSE
├── exambank/
├── data/
└── tests/
```

### ขั้นตอนที่ 8: ติดตั้งและรันโปรแกรม
💻 เปิด Command Prompt หรือ Terminal ในโฟลเดอร์นี้

```bash
# ติดตั้ง dependencies
pip install -r requirements.txt

# รันโปรแกรม
python app.py
```

---

## 🎯 ทางเลือกอื่น: ใช้ Git Clone

ถ้าคุณมี Git ติดตั้งอยู่แล้ว สามารถใช้คำสั่งนี้:

```bash
git clone https://github.com/kornxi/exambank-system.git
cd exambank-system
```

**ข้อดีของ Git Clone:**
- ✅ สามารถ pull updates ได้
- ✅ เก็บประวัติการเปลี่ยนแปลง
- ✅ สามารถ contribute กลับได้

**ข้อดีของ Download ZIP:**
- ✅ ไม่ต้องติดตั้ง Git
- ✅ ใช้งานได้ทันที
- ✅ เหมาะสำหรับผู้ใช้ทั่วไป

---

## 📊 เปรียบเทียบวิธีการดาวน์โหลด

| คุณสมบัติ | Download ZIP | Git Clone |
|-----------|--------------|-----------|
| ต้องติดตั้ง Git | ❌ ไม่ต้อง | ✅ ต้อง |
| ความเร็ว | ⚡ เร็ว | ⚡ เร็ว |
| อัปเดตได้ | ❌ ต้องดาวน์โหลดใหม่ | ✅ `git pull` |
| ขนาด | 📦 50 KB | 📦 ~200 KB (รวม .git) |
| เหมาะสำหรับ | ผู้ใช้ทั่วไป | นักพัฒนา |

---

## ❓ คำถามที่พบบ่อย

### Q: ดาวน์โหลดไฟล์ไปแล้ว ทำอะไรต่อ?
A: แตกไฟล์ ZIP แล้วติดตั้ง Python dependencies ด้วย `pip install -r requirements.txt` จากนั้นรันด้วย `python app.py`

### Q: ต้องมี Internet ในการใช้งานไหม?
A: ไม่ต้อง! หลังจากดาวน์โหลดและติดตั้งแล้ว ใช้งานได้แบบ offline

### Q: สามารถแก้ไขโค้ดได้ไหม?
A: ได้! ระบบใช้ MIT License แก้ไขและใช้งานได้ตามต้องการ

### Q: ถ้าดาวน์โหลด ZIP แล้วระบบมีการอัปเดตจะทำยังไง?
A: ดาวน์โหลด ZIP ใหม่ หรือเปลี่ยนมาใช้ Git clone แทน

### Q: ไฟล์ ZIP มีขนาดเท่าไหร่?
A: ประมาณ 50 KB (ไม่รวม .git folder)

### Q: ใช้ได้บนระบบปฏิบัติการอะไรบ้าง?
A: Windows, macOS, และ Linux ทุกระบบที่มี Python 3.7+

---

## 🎓 ขั้นตอนสำหรับผู้เริ่มต้น

### 1. ติดตั้ง Python (ถ้ายังไม่มี)
- ดาวน์โหลดจาก: https://www.python.org/downloads/
- ติดตั้งตามขั้นตอน (เลือก "Add Python to PATH")

### 2. ตรวจสอบ Python
เปิด Command Prompt/Terminal แล้วพิมพ์:
```bash
python --version
```
ควรแสดง: `Python 3.x.x`

### 3. ดาวน์โหลดระบบ
ตามขั้นตอนด้านบน (Download ZIP)

### 4. ติดตั้ง Dependencies
```bash
cd exambank-system-main
pip install -r requirements.txt
```

### 5. ทดสอบระบบ
```bash
python app.py list
```

ถ้าเห็นรายการคำถาม แสดงว่าติดตั้งสำเร็จ! 🎉

---

## 📞 ต้องการความช่วยเหลือ?

หากพบปัญหาในการดาวน์โหลดหรือติดตั้ง:
1. อ่าน USAGE.md สำหรับคู่มือโดยละเอียด
2. อ่าน EXAMPLES.md สำหรับตัวอย่างการใช้งาน
3. สร้าง Issue บน GitHub: https://github.com/kornxi/exambank-system/issues

---

**สรุป:** ดาวน์โหลด ZIP → แตกไฟล์ → ติดตั้ง Dependencies → รันโปรแกรม ✅
