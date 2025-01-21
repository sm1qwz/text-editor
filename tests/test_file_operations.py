import unittest
from editor.file_operations import open_file, save_file
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestFileOperations(unittest.TestCase):
    """
    Тесты для модуля работы с файлами.
    """

    def test_open_file(self):
        """
        Тестирует функцию открытия файла.
        """
        content = open_file('test_file.txt')
        self.assertIn("Hello", content)

    def test_save_file(self):
        """
        Тестирует функцию сохранения файла.
        """
        save_file('test_save.txt', 'Test content')
        content = open_file('test_save.txt')
        self.assertEqual(content, 'Test content')
