print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.


limit = int(input('Введите предел вычислений: '))
num = 1
while num <= limit:
  print(num, 'в степени 3 = ', num**3)
  num += 1