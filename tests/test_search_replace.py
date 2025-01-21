import unittest
from editor.search_replace import search_text, replace_text
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestSearchReplace(unittest.TestCase):
    """
    Тесты для модуля поиска и замены текста.
    """

    def test_search_text(self):
        """
        Тестирует функцию поиска текста.
        """
        content = "Hello, world!"
        search_text(content, "world")
        self.assertIn("world", content)

    def test_replace_text(self):
        """
        Тестирует функцию замены текста.
        """
        content = "Hello, world!"
        new_content = replace_text(content, "world:Earth")
        self.assertEqual(new_content, "Hello, Earth!")
