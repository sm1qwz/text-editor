"""
Модуль для подсветки синтаксиса простых языков программирования.
"""

import re

def highlight_syntax(content):
    """
    Подсвечивает синтаксис простых языков программирования (например, Python).

    :param content: Текстовый код для подсветки.
    :type content: str
    :return: Текст с подсветкой синтаксиса.
    :rtype: str
    :raises: Нет.
    """
    keywords = r'\b(def|class|import|if|else|for|while|return)\b'
    functions = r'\b\w+\(.*\)\b'
    strings = r'"[^"]*"'

    # Подсветка ключевых слов
    content = re.sub(keywords, r'\033[1;32m\g<0>\033[0m', content)
    # Подсветка функций
    content = re.sub(functions, r'\033[1;34m\g<0>\033[0m', content)
    # Подсветка строк
    content = re.sub(strings, r'\033[1;31m\g<0>\033[0m', content)

    return content
