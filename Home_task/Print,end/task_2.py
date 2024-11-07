print('Задача 2. Я стал новым пиратом!')

pirat_count =0
for real_pirat in range(0,10):
    pirat =input('Введите слово: ')
    if (pirat == 'Карамба') or (pirat == 'карамба'):
        pirat_count +=1

print('Кол-во настоящих пиратов: ',pirat_count)