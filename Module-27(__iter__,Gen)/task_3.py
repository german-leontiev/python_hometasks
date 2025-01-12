# Задача 3. Пути файлов
# Что нужно сделать
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории (по умолчанию — корневой диск), 
# находит указанный пользователем каталог и генерирует пути всех встреченных файлов.

# Решение задачи должно быть без рекурсии.

import os

def Main(target_dir=None):
    root_dir = os.getcwd()
    stack = [root_dir]
    while stack:
        current_dir = stack.pop()
        print(f"Обрабатываем каталог: {current_dir}")
        try:
            for entry in os.scandir(current_dir):
                if entry.is_file():
                    print(f"Найден файл: {entry.path}")
                    if target_dir is None or os.path.basename(current_dir) == target_dir:
                        print(f"Файл соответствует условиям: {entry.path}")
                        yield entry.path
                elif entry.is_dir():
                    print(f"Найден подкаталог: {entry.path}")
                    stack.append(entry.path)
        except PermissionError:
            print(f"Нет доступа к каталогу: {current_dir}")

target_dir = 'task_3'
for file_path in Main(target_dir):
    print(f"Выводим путь файла: {file_path}")