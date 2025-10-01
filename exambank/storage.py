"""
Storage module for managing JSON data files
จัดการการเก็บข้อมูลในรูปแบบ JSON
"""

import json
import os
from typing import List, Dict, Any


class Storage:
    """จัดการการอ่านและเขียนข้อมูล JSON"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def load_json(self, filename: str) -> List[Dict[str, Any]]:
        """อ่านข้อมูลจากไฟล์ JSON"""
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            return []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    
    def save_json(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """บันทึกข้อมูลลงไฟล์ JSON"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
