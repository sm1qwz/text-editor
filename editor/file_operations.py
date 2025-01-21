"""
Модуль для работы с файлами.
"""

def open_file(file_path):
    """
    Открывает файл и возвращает его содержимое.

    :param file_path: Путь к файлу, который нужно открыть.
    :type file_path: str
    :return: Содержимое файла в виде строки.
    :rtype: str

    :raises FileNotFoundError: Если файл не найден.
    :raises IOError: Если произошла ошибка при открытии файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return ""
    except IOError as e:
        print(f"Ошибка при открытии файла: {e}")
        return ""

def save_file(file_path, content):
    """
    Сохраняет содержимое в файл.

    :param file_path: Путь к файлу, в который нужно сохранить содержимое.
    :type file_path: str
    :param content: Содержимое, которое нужно сохранить в файл.
    :type content: str
    :return: Нет.
    :raises IOError: Если произошла ошибка при сохранении файла.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")
