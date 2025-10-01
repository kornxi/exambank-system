"""
Question module for managing exam questions
โมดูลจัดการคำถามข้อสอบ
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid


class Question:
    """คลาสสำหรับจัดการคำถามข้อสอบ"""
    
    def __init__(self, storage):
        self.storage = storage
        self.filename = "questions.json"
    
    def add(self, text: str, choices: List[str], correct_answer: int, 
            subject: str, topic: str, difficulty: str = "medium") -> Dict:
        """เพิ่มคำถามใหม่"""
        questions = self.storage.load_json(self.filename)
        
        question = {
            "id": str(uuid.uuid4()),
            "text": text,
            "choices": choices,
            "correct_answer": correct_answer,
            "subject": subject,
            "topic": topic,
            "difficulty": difficulty,
            "created_at": datetime.now().isoformat()
        }
        
        questions.append(question)
        self.storage.save_json(self.filename, questions)
        return question
    
    def get_all(self) -> List[Dict]:
        """ดึงคำถามทั้งหมด"""
        return self.storage.load_json(self.filename)
    
    def get_by_id(self, question_id: str) -> Optional[Dict]:
        """ดึงคำถามตาม ID"""
        questions = self.get_all()
        for q in questions:
            if q["id"] == question_id:
                return q
        return None
    
    def search(self, keyword: str) -> List[Dict]:
        """ค้นหาคำถามด้วยคำสำคัญ"""
        questions = self.get_all()
        keyword_lower = keyword.lower()
        return [
            q for q in questions 
            if keyword_lower in q["text"].lower() 
            or keyword_lower in q.get("subject", "").lower()
            or keyword_lower in q.get("topic", "").lower()
        ]
    
    def filter_by_subject(self, subject: str) -> List[Dict]:
        """กรองคำถามตามวิชา"""
        questions = self.get_all()
        return [q for q in questions if q.get("subject") == subject]
    
    def filter_by_difficulty(self, difficulty: str) -> List[Dict]:
        """กรองคำถามตามความยาก"""
        questions = self.get_all()
        return [q for q in questions if q.get("difficulty") == difficulty]
    
    def delete(self, question_id: str) -> bool:
        """ลบคำถาม"""
        questions = self.get_all()
        new_questions = [q for q in questions if q["id"] != question_id]
        
        if len(new_questions) < len(questions):
            self.storage.save_json(self.filename, new_questions)
            return True
        return False
    
    def update(self, question_id: str, updates: Dict) -> Optional[Dict]:
        """อัปเดตคำถาม"""
        questions = self.get_all()
        
        for i, q in enumerate(questions):
            if q["id"] == question_id:
                questions[i].update(updates)
                questions[i]["updated_at"] = datetime.now().isoformat()
                self.storage.save_json(self.filename, questions)
                return questions[i]
        
        return None
