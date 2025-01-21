import unittest
from editor.file_operations import open_file, save_file
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestFileOperations(unittest.TestCase):
    def test_open_file(self):
        content = open_file('test_file.txt')
        self.assertIn("Hello", content)

    def test_save_file(self):
        save_file('test_save.txt', 'Test content')
        content = open_file('test_save.txt')
        self.assertEqual(content, 'Test content')
