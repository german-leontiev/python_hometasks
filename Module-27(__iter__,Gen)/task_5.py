# Задача 5. Количество строк
# Что нужно сделать
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет общее количество строк кода, 
# игнорируя пустые строки и строчки комментариев.

import os

def Main(dir):
    total_count = 0
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_count = sum(1 for line in file if line.strip() and not line.startswith('#'))
                    total_count += file_count
                    yield file_path, file_count
    yield None, total_count

for file_path, count in Main('.'):
    if file_path is not None:
        print(f'Файл: {file_path}, Общее количество строк кода: {count}')
    else:
        print(f'Общее количество строк кода во всех файлах: {count}')