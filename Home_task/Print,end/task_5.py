print('Задача 5. Марсоход 2')





startA = 8
startB = 10
op = ''
while op != 'Stop':
    op =input('введите команду:')
    for symbol in op:
        print('[Программа]: Марсоход находится на позиции ',startA , startB,)
        if symbol =='a' or symbol == 'A':
            startA -=1  
        elif symbol == 'd' or symbol == 'D':
            startA += 1
        elif symbol == 'w' or symbol == 'W':
            startB += 1
        elif symbol == 's' or symbol == 'S':
            startB -= 1
        elif startA == 15:
            startA -= 1
        if startA == 0:
            startA += 1
            print('Стена,вернулись на прошлую позицию ',startA,startB)
        elif startB == 20:
            startB -= 1
            print('Стена,вернулись на прошлую позицию ',startA,startB)







              

