import unittest
from editor.syntax_highlighting import highlight_syntax
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestSyntaxHighlighting(unittest.TestCase):
    def test_highlight_syntax(self):
        code = 'def hello():\n    print("Hello, world!")'
        highlighted = highlight_syntax(code)
        self.assertIn('\033[1;32mdef\033[0m', highlighted)  # Подсветка ключевых слов
        self.assertIn('hello', highlighted)  # Простое наличие слова
