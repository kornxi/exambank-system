"""
Exam module for creating and managing exam sets
โมดูลจัดการชุดข้อสอบ
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
import random


class Exam:
    """คลาสสำหรับจัดการชุดข้อสอบ"""
    
    def __init__(self, storage, question_manager):
        self.storage = storage
        self.question_manager = question_manager
        self.filename = "exams.json"
    
    def create(self, title: str, subject: str, num_questions: int, 
               difficulty: Optional[str] = None) -> Dict:
        """สร้างชุดข้อสอบใหม่"""
        # ดึงคำถามตามเงื่อนไข
        questions = self.question_manager.filter_by_subject(subject)
        
        if difficulty:
            questions = [q for q in questions if q.get("difficulty") == difficulty]
        
        # สุ่มเลือกคำถาม
        if len(questions) < num_questions:
            num_questions = len(questions)
        
        selected_questions = random.sample(questions, num_questions)
        
        exam = {
            "id": str(uuid.uuid4()),
            "title": title,
            "subject": subject,
            "difficulty": difficulty,
            "questions": [q["id"] for q in selected_questions],
            "created_at": datetime.now().isoformat()
        }
        
        exams = self.storage.load_json(self.filename)
        exams.append(exam)
        self.storage.save_json(self.filename, exams)
        
        return exam
    
    def get_all(self) -> List[Dict]:
        """ดึงชุดข้อสอบทั้งหมด"""
        return self.storage.load_json(self.filename)
    
    def get_by_id(self, exam_id: str) -> Optional[Dict]:
        """ดึงชุดข้อสอบตาม ID"""
        exams = self.get_all()
        for exam in exams:
            if exam["id"] == exam_id:
                return exam
        return None
    
    def get_exam_with_questions(self, exam_id: str) -> Optional[Dict]:
        """ดึงชุดข้อสอบพร้อมคำถามเต็ม"""
        exam = self.get_by_id(exam_id)
        if not exam:
            return None
        
        questions = []
        for q_id in exam["questions"]:
            question = self.question_manager.get_by_id(q_id)
            if question:
                questions.append(question)
        
        exam_with_questions = exam.copy()
        exam_with_questions["questions"] = questions
        
        return exam_with_questions
    
    def delete(self, exam_id: str) -> bool:
        """ลบชุดข้อสอบ"""
        exams = self.get_all()
        new_exams = [e for e in exams if e["id"] != exam_id]
        
        if len(new_exams) < len(exams):
            self.storage.save_json(self.filename, new_exams)
            return True
        return False
