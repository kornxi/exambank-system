"""Tests for storage module"""

import os
import tempfile
import shutil
import pytest
from exambank.storage import Storage


class TestStorage:
    """Test Storage class"""
    
    def setup_method(self):
        """Setup test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.storage = Storage(self.test_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_and_load_json(self):
        """Test saving and loading JSON data"""
        test_data = [
            {"id": "1", "name": "Test"},
            {"id": "2", "name": "Test2"}
        ]
        
        # Save data
        result = self.storage.save_json("test.json", test_data)
        assert result is True
        
        # Load data
        loaded_data = self.storage.load_json("test.json")
        assert loaded_data == test_data
    
    def test_load_nonexistent_file(self):
        """Test loading non-existent file returns empty list"""
        data = self.storage.load_json("nonexistent.json")
        assert data == []
    
    def test_data_directory_creation(self):
        """Test that data directory is created"""
        new_dir = os.path.join(self.test_dir, "new_storage")
        storage = Storage(new_dir)
        assert os.path.exists(new_dir)
