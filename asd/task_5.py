print('Задача 5. Функция')
#Что нужно сделать
#Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. Помогите Саше
#написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).
#
#Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный), а затем высчитывает
#функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.
#Сама функция выглядит так:
# y = (x **3) + (2* x **2) - (4 * x) +1
start =int(input('Введите начало отрезка: '))
stop =int(input('Введите конец отрезка: '))
step =int(input('Введите шаг: '))
if step > 0:
    step = -step
for cut in range(stop, start -1, step):
    function = (cut **3) + (2* cut**2) - (4 * cut) + 1
    print('В точке', cut , 'функция равна: ', function)