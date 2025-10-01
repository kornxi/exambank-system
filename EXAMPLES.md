# ตัวอย่างการใช้งาน (Usage Examples)

## ตัวอย่างที่ 1: ดูคำถามทั้งหมด

```bash
$ python app.py list
```

**ผลลัพธ์:**
```
--- คำถามทั้งหมด ---

1. [Python Programming] Python ใช้คำสั่งใดในการแสดงผลลัพธ์?
     1. echo()
   ✓ 2. print()
     3. console.log()
     4. printf()
   ความยาก: easy

2. [Python Programming] ข้อใดคือ data type ใน Python?
     1. int
     2. string
     3. list
   ✓ 4. ถูกทุกข้อ
   ความยาก: easy

3. [Python Programming] อะไรคือผลลัพธ์ของ 2 ** 3 ใน Python?
     1. 6
   ✓ 2. 8
     3. 9
     4. 5
   ความยาก: medium
```

## ตัวอย่างที่ 2: ค้นหาคำถาม

```bash
$ python app.py search "Python"
```

**ผลลัพธ์:**
```
Found 3 questions
```

## ตัวอย่างที่ 3: เพิ่มคำถามใหม่ (Interactive Mode)

```bash
$ python app.py
```

เลือก **1** เพื่อเพิ่มคำถาม:

```
--- เพิ่มคำถามใหม่ ---
คำถาม (Question): What is 1+1?
ตัวเลือก 1 (Choice 1): 1
ตัวเลือก 2 (Choice 2): 2
ตัวเลือก 3 (Choice 3): 3
ตัวเลือก 4 (Choice 4): 4
คำตอบที่ถูกต้อง (Correct answer 1-4): 2
วิชา (Subject): Mathematics
หัวข้อ (Topic): Basic Arithmetic
ระดับความยาก (Difficulty - easy/medium/hard): easy

✓ เพิ่มคำถามสำเร็จ! ID: 123e4567-e89b-12d3-a456-426614174000
```

## ตัวอย่างที่ 4: สร้างชุดข้อสอบ

```bash
$ python app.py
```

เลือก **4** เพื่อสร้างชุดข้อสอบ:

```
--- สร้างชุดข้อสอบใหม่ ---
ชื่อชุดข้อสอบ (Exam title): Python Midterm Exam
วิชา (Subject): Python Programming
จำนวนข้อ (Number of questions): 3
ระดับความยาก (Difficulty - leave blank for all): 

✓ สร้างชุดข้อสอบสำเร็จ! ID: 987f6543-e21b-34d5-b678-537725285111
จำนวนข้อ: 3
```

## ตัวอย่างที่ 5: ดูชุดข้อสอบทั้งหมด

เลือก **5** จากเมนูหลัก:

```
--- ชุดข้อสอบทั้งหมด ---

1. Python Basics Test
   วิชา: Python Programming
   จำนวนข้อ: 2
   ID: exam-001

2. Python Midterm Exam
   วิชา: Python Programming
   จำนวนข้อ: 3
   ID: 987f6543-e21b-34d5-b678-537725285111
```

## ตัวอย่างที่ 6: ดูรายละเอียดชุดข้อสอบ

เลือก **6** และใส่ ID ของชุดข้อสอบ:

```
ใส่ ID ของชุดข้อสอบ: exam-001

==================================================
ชุดข้อสอบ: Python Basics Test
วิชา: Python Programming
==================================================

ข้อ 1. Python ใช้คำสั่งใดในการแสดงผลลัพธ์?
   1. echo()
   2. print()
   3. console.log()
   4. printf()

ข้อ 2. ข้อใดคือ data type ใน Python?
   1. int
   2. string
   3. list
   4. ถูกทุกข้อ
```

## ตัวอย่างการทดสอบ (Testing)

```bash
$ python -m pytest tests/ -v
```

**ผลลัพธ์:**
```
================================================= test session starts ==================================================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: /home/runner/work/exambank-system/exambank-system
collecting ... collected 8 items

tests/test_question.py::TestQuestion::test_add_question PASSED                    [ 12%]
tests/test_question.py::TestQuestion::test_get_all_questions PASSED               [ 25%]
tests/test_question.py::TestQuestion::test_search_questions PASSED                [ 37%]
tests/test_question.py::TestQuestion::test_filter_by_subject PASSED               [ 50%]
tests/test_question.py::TestQuestion::test_delete_question PASSED                 [ 62%]
tests/test_storage.py::TestStorage::test_save_and_load_json PASSED                [ 75%]
tests/test_storage.py::TestStorage::test_load_nonexistent_file PASSED             [ 87%]
tests/test_storage.py::TestStorage::test_data_directory_creation PASSED           [100%]

================================================== 8 passed in 0.03s ===================================================
```

## การใช้งาน Python API

```python
from exambank.storage import Storage
from exambank.question import Question
from exambank.exam import Exam

# Initialize
storage = Storage()
question_manager = Question(storage)
exam_manager = Exam(storage, question_manager)

# Add a question
question = question_manager.add(
    text="What is Python?",
    choices=["A language", "A snake", "A tool", "All above"],
    correct_answer=0,
    subject="Python",
    topic="Introduction",
    difficulty="easy"
)

# Search questions
results = question_manager.search("Python")
print(f"Found {len(results)} questions")

# Create an exam
exam = exam_manager.create(
    title="Python Test",
    subject="Python",
    num_questions=5
)
print(f"Created exam with {len(exam['questions'])} questions")
```

## โครงสร้างข้อมูล JSON

### questions.json
```json
[
  {
    "id": "sample-001",
    "text": "Python ใช้คำสั่งใดในการแสดงผลลัพธ์?",
    "choices": ["echo()", "print()", "console.log()", "printf()"],
    "correct_answer": 1,
    "subject": "Python Programming",
    "topic": "Basic Syntax",
    "difficulty": "easy",
    "created_at": "2025-01-01T00:00:00"
  }
]
```

### exams.json
```json
[
  {
    "id": "exam-001",
    "title": "Python Basics Test",
    "subject": "Python Programming",
    "difficulty": "easy",
    "questions": ["sample-001", "sample-002"],
    "created_at": "2025-01-01T00:00:00"
  }
]
```
