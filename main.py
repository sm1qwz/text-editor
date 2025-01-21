import argparse
import os
from editor.file_operations import open_file, save_file
from editor.search_replace import search_text, replace_text
from editor.syntax_highlighting import highlight_syntax


def validate_replace(value):
    """
    Проверяет, что аргумент --replace имеет правильный формат old:new.

    :param value: Значение аргумента --replace
    :return: Возвращает значение аргумента, если формат правильный, или выводит предупреждение.

    :raises: Нет
    """
    if ":" not in value:
        print("Предупреждение: Аргумент --replace не содержит ':'. Используйте формат 'old:new'.")
        return value
    return value


def count_statistics(content):
    """
    Подсчитывает количество строк, слов и символов в содержимом текста.

    :param content: Содержимое текста
    :type content: str
    :return: Кортеж с количеством строк, слов и символов
    :rtype: tuple
    """
    lines = content.splitlines()
    words = content.split()
    characters = len(content)
    return len(lines), len(words), characters


def delete_file(filename):
    """
    Удаляет файл из директории.

    :param filename: Имя файла для удаления
    :type filename: str
    :return: Нет
    :raises FileNotFoundError: Если файл не найден
    :raises Exception: Если возникла другая ошибка при удалении
    """
    try:
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")


def main():
    """
    Главная функция программы. Обрабатывает командную строку, выполняет операции с файлами,
    такими как открытие, сохранение, поиск, замена текста, подсветка синтаксиса и удаление файлов.

    :return: Нет
    :raises: Нет
    """
    parser = argparse.ArgumentParser(description="Текстовый редактор.")
    parser.add_argument("--open", type=str, help="Открыть файл.")
    parser.add_argument("--save", type=str, help="Сохранить файл.")
    parser.add_argument("--search", type=str, help="Поиск текста в файле.")
    parser.add_argument("--replace", type=validate_replace, help="Заменить текст в формате 'old:new'.")
    parser.add_argument("--highlight", action='store_true', help="Подсветка синтаксиса.")
    parser.add_argument("--stats", action='store_true', help="Подсчитать статистику текста.")
    parser.add_argument("--delete", type=str, help="Удалить файл из директории.")

    args = parser.parse_args()

    content = None  # Для хранения содержимого открытого файла

    if args.open:
        try:
            content = open_file(args.open)
            print("Файл успешно открыт. Содержимое:")
            print(content)
        except FileNotFoundError:
            print(f"Ошибка: файл {args.open} не найден.")
            return
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")
            return

    if args.search:
        if content is not None:
            search_text(content, args.search)
        else:
            print("Нет открытого файла для поиска.")

    if args.replace:
        if content is not None:
            try:
                old, new = args.replace.split(":")
                content = replace_text(content, f"{old}:{new}")
                print("Текст успешно заменен. Новое содержимое:")
                print(content)
            except Exception as e:
                print(f"Ошибка при замене текста: {e}")
        else:
            print("Нет открытого файла для замены.")

    if args.highlight:
        if content is not None:
            highlighted_content = highlight_syntax(content)
            print("Синтаксис подсвечен. Результат:")
            print(highlighted_content)
        else:
            print("Нет открытого файла для подсветки синтаксиса.")

    if args.stats:
        if content is not None:
            lines, words, chars = count_statistics(content)
            print(f"Статистика файла: {lines} строк, {words} слов, {chars} символов.")
        else:
            print("Нет открытого файла для подсчета статистики.")

    if args.save:
        if content is not None:
            try:
                save_file(args.save, content)
                print(f"Файл успешно сохранен в {args.save}")
            except Exception as e:
                print(f"Ошибка при сохранении файла: {e}")
        else:
            print("Нет содержимого для сохранения.")

    if args.delete:
        delete_file(args.delete)


if __name__ == "__main__":
    main()
