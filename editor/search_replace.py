"""
Модуль для поиска и замены текста.
"""
def search_text(content, search_term):
    """Поиск текста в содержимом."""
    if search_term in content:
        print(f"Текст '{search_term}' найден.")
    else:
        print(f"Текст '{search_term}' не найден.")

def replace_text(content, replace_term):
    """Замена текста в содержимом."""
    old, new = replace_term.split(":")
    content = content.replace(old, new)
    return content
