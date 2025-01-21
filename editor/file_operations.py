"""
Модуль для работы с файлами.
"""
def open_file(file_path):
    """Открытие файла и возвращение его содержимого."""
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
    """Сохранение содержимого в файл."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")
