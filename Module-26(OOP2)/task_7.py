# Задача 7. Стек
# Что нужно сделать
# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры данных на основе уже существующих. 
# Одной из таких «базовых» структур является стек.

# Стек — это абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»). 

# Простой пример: стек из книг на столе. Единственной книгой, чья обложка видна, является самая верхняя. 
# Чтобы получить доступ к, например, третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.

# Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента). 

# После этого напишите ещё один класс — «Менеджер задач». 
# В менеджере задач можно выполнить команду «Новая задача», в которую передаётся сама задача (str) и её приоритет (int). 
# Сам менеджер работает на основе стека (не наследование!). При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача. 

# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager) 

# Результат:
# 1 отдохнуть
# 2 поесть; сдать дз
# 4 сделать уборку; помыть посуду 

# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.