"""Tests for question module"""

import os
import tempfile
import shutil
import pytest
from exambank.storage import Storage
from exambank.question import Question


class TestQuestion:
    """Test Question class"""
    
    def setup_method(self):
        """Setup test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.storage = Storage(self.test_dir)
        self.question_manager = Question(self.storage)
    
    def teardown_method(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_add_question(self):
        """Test adding a new question"""
        question = self.question_manager.add(
            "What is Python?",
            ["A language", "A snake", "A software", "A tool"],
            0,
            "Python",
            "Introduction",
            "easy"
        )
        
        assert question["text"] == "What is Python?"
        assert len(question["choices"]) == 4
        assert question["correct_answer"] == 0
        assert "id" in question
    
    def test_get_all_questions(self):
        """Test getting all questions"""
        self.question_manager.add(
            "Question 1", ["A", "B", "C", "D"], 0, "Subject1", "Topic1"
        )
        self.question_manager.add(
            "Question 2", ["A", "B", "C", "D"], 1, "Subject2", "Topic2"
        )
        
        questions = self.question_manager.get_all()
        assert len(questions) == 2
    
    def test_search_questions(self):
        """Test searching questions"""
        self.question_manager.add(
            "Python is great", ["A", "B", "C", "D"], 0, "Programming", "Python"
        )
        self.question_manager.add(
            "Java is also good", ["A", "B", "C", "D"], 1, "Programming", "Java"
        )
        
        results = self.question_manager.search("Python")
        assert len(results) == 1
        assert "Python" in results[0]["text"]
    
    def test_filter_by_subject(self):
        """Test filtering by subject"""
        self.question_manager.add(
            "Q1", ["A", "B", "C", "D"], 0, "Math", "Algebra"
        )
        self.question_manager.add(
            "Q2", ["A", "B", "C", "D"], 1, "Science", "Physics"
        )
        
        math_questions = self.question_manager.filter_by_subject("Math")
        assert len(math_questions) == 1
        assert math_questions[0]["subject"] == "Math"
    
    def test_delete_question(self):
        """Test deleting a question"""
        question = self.question_manager.add(
            "Test", ["A", "B", "C", "D"], 0, "Test", "Test"
        )
        
        result = self.question_manager.delete(question["id"])
        assert result is True
        
        questions = self.question_manager.get_all()
        assert len(questions) == 0
