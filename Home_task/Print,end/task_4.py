print('Задача 4. Театр')

line =int(input('Введите кол-во рядов: '))
chair =int(input('Введите кол-во сидений: '))
metr =int(input('Введите кол-во метров между сидений: '))

print('\nСцена')
for scenes in range(line):
    line = '=' * chair
    scene = line + '*' * metr + line
    print(scene)
