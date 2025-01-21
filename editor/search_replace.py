"""
Модуль для поиска и замены текста.
"""

def search_text(content, search_term):
    """
    Ищет указанный текст в содержимом и выводит, найден ли он.

    :param content: Содержимое, в котором производится поиск.
    :type content: str
    :param search_term: Текст, который нужно найти.
    :type search_term: str
    :return: Нет.
    :raises: Нет.
    """
    if search_term in content:
        print(f"Текст '{search_term}' найден.")
    else:
        print(f"Текст '{search_term}' не найден.")

def replace_text(content, replace_term):
    """
    Заменяет старый текст новым в содержимом.

    :param content: Содержимое, в котором производится замена.
    :type content: str
    :param replace_term: Текст в формате 'old:new', где old — это текст для замены, а new — новый текст.
    :type replace_term: str
    :return: Измененное содержимое с выполненной заменой.
    :rtype: str
    :raises: ValueError: Если формат строки для замены некорректен.
    """
    old, new = replace_term.split(":")
    content = content.replace(old, new)
    return content
