#!/usr/bin/env python3
"""
Exam Bank System - Main Application
ระบบธนาคารข้อสอบ - แอปพลิเคชันหลัก
"""

import sys
from exambank.storage import Storage
from exambank.question import Question
from exambank.exam import Exam


def print_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*50)
    print("ระบบธนาคารข้อสอบ (Exam Bank System)")
    print("="*50)
    print("1. เพิ่มคำถามใหม่ (Add Question)")
    print("2. แสดงคำถามทั้งหมด (List All Questions)")
    print("3. ค้นหาคำถาม (Search Questions)")
    print("4. สร้างชุดข้อสอบ (Create Exam)")
    print("5. แสดงชุดข้อสอบ (List Exams)")
    print("6. ดูรายละเอียดชุดข้อสอบ (View Exam Details)")
    print("7. ลบคำถาม (Delete Question)")
    print("0. ออกจากระบบ (Exit)")
    print("="*50)


def add_question(question_manager):
    """เพิ่มคำถามใหม่"""
    print("\n--- เพิ่มคำถามใหม่ ---")
    text = input("คำถาม (Question): ")
    
    choices = []
    for i in range(4):
        choice = input(f"ตัวเลือก {i+1} (Choice {i+1}): ")
        choices.append(choice)
    
    correct = int(input("คำตอบที่ถูกต้อง (Correct answer 1-4): ")) - 1
    subject = input("วิชา (Subject): ")
    topic = input("หัวข้อ (Topic): ")
    difficulty = input("ระดับความยาก (Difficulty - easy/medium/hard): ") or "medium"
    
    question = question_manager.add(text, choices, correct, subject, topic, difficulty)
    print(f"\n✓ เพิ่มคำถามสำเร็จ! ID: {question['id']}")


def list_questions(question_manager):
    """แสดงคำถามทั้งหมด"""
    print("\n--- คำถามทั้งหมด ---")
    questions = question_manager.get_all()
    
    if not questions:
        print("ยังไม่มีคำถามในระบบ")
        return
    
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. [{q['subject']}] {q['text']}")
        for j, choice in enumerate(q['choices'], 1):
            marker = "✓" if j-1 == q['correct_answer'] else " "
            print(f"   {marker} {j}. {choice}")
        print(f"   ความยาก: {q.get('difficulty', 'N/A')}")


def search_questions(question_manager):
    """ค้นหาคำถาม"""
    keyword = input("\nคำสำคัญที่ต้องการค้นหา: ")
    questions = question_manager.search(keyword)
    
    if not questions:
        print("ไม่พบคำถามที่ตรงกับคำค้นหา")
        return
    
    print(f"\nพบ {len(questions)} คำถาม:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. [{q['subject']}] {q['text'][:50]}...")


def create_exam(exam_manager):
    """สร้างชุดข้อสอบ"""
    print("\n--- สร้างชุดข้อสอบใหม่ ---")
    title = input("ชื่อชุดข้อสอบ (Exam title): ")
    subject = input("วิชา (Subject): ")
    num_questions = int(input("จำนวนข้อ (Number of questions): "))
    difficulty = input("ระดับความยาก (Difficulty - leave blank for all): ") or None
    
    exam = exam_manager.create(title, subject, num_questions, difficulty)
    print(f"\n✓ สร้างชุดข้อสอบสำเร็จ! ID: {exam['id']}")
    print(f"จำนวนข้อ: {len(exam['questions'])}")


def list_exams(exam_manager):
    """แสดงชุดข้อสอบทั้งหมด"""
    print("\n--- ชุดข้อสอบทั้งหมด ---")
    exams = exam_manager.get_all()
    
    if not exams:
        print("ยังไม่มีชุดข้อสอบในระบบ")
        return
    
    for i, exam in enumerate(exams, 1):
        print(f"\n{i}. {exam['title']}")
        print(f"   วิชา: {exam['subject']}")
        print(f"   จำนวนข้อ: {len(exam['questions'])}")
        print(f"   ID: {exam['id']}")


def view_exam_details(exam_manager):
    """ดูรายละเอียดชุดข้อสอบ"""
    exam_id = input("\nใส่ ID ของชุดข้อสอบ: ")
    exam = exam_manager.get_exam_with_questions(exam_id)
    
    if not exam:
        print("ไม่พบชุดข้อสอบ")
        return
    
    print(f"\n{'='*50}")
    print(f"ชุดข้อสอบ: {exam['title']}")
    print(f"วิชา: {exam['subject']}")
    print(f"{'='*50}")
    
    for i, q in enumerate(exam['questions'], 1):
        print(f"\nข้อ {i}. {q['text']}")
        for j, choice in enumerate(q['choices'], 1):
            print(f"   {j}. {choice}")


def delete_question(question_manager):
    """ลบคำถาม"""
    question_id = input("\nใส่ ID ของคำถามที่ต้องการลบ: ")
    
    if question_manager.delete(question_id):
        print("✓ ลบคำถามสำเร็จ!")
    else:
        print("✗ ไม่พบคำถาม")


def main():
    """ฟังก์ชันหลัก"""
    # Initialize system
    storage = Storage()
    question_manager = Question(storage)
    exam_manager = Exam(storage, question_manager)
    
    # Command line mode
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            list_questions(question_manager)
        elif command == "search" and len(sys.argv) > 2:
            questions = question_manager.search(sys.argv[2])
            print(f"Found {len(questions)} questions")
        else:
            print(f"Unknown command: {command}")
        
        return
    
    # Interactive mode
    while True:
        print_menu()
        choice = input("\nเลือกเมนู (Choose option): ")
        
        try:
            if choice == "0":
                print("\nขอบคุณที่ใช้บริการ!")
                break
            elif choice == "1":
                add_question(question_manager)
            elif choice == "2":
                list_questions(question_manager)
            elif choice == "3":
                search_questions(question_manager)
            elif choice == "4":
                create_exam(exam_manager)
            elif choice == "5":
                list_exams(exam_manager)
            elif choice == "6":
                view_exam_details(exam_manager)
            elif choice == "7":
                delete_question(question_manager)
            else:
                print("\n✗ กรุณาเลือกเมนูที่ถูกต้อง")
        
        except Exception as e:
            print(f"\n✗ เกิดข้อผิดพลาด: {e}")
        
        input("\nกด Enter เพื่อดำเนินการต่อ...")


if __name__ == "__main__":
    main()
