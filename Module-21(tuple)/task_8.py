# Задача 8. Контакты 3
# Мы уже помогали Степану с реализацией телефонной книги (контактов) на телефоне, 
# однако внезапно оказалось, что книге не хватает ещё одной очень полезной функции: поиска!

# Напишите программу, которая бесконечно запрашивает у пользователя действие, 
# которое он хочет совершить: добавить контакт или найти человека в списке контактов по фамилии. 

# Действие «Добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона, 
# добавляет их в словарь и выводит на экран текущий словарь контактов. 
# Если этот человек уже есть в словаре, то выведите соответствующее сообщение.

# Действие «Поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией и их номера телефонов. 
# Поиск не должен зависеть от регистра символов.

phonebook = {
    ('Петров','Ваня'): 889993,
    ('Егоров','Петя'): 889098,
    ('Ульянов','Петя'): 880898,
    ('Сидорова','Лена'): 876126,
    ('Сидоров','Женя'):856343
}

while True:
    text =int(input('1 - Добавить контакт, 2 - Поиск человека по фамилии, 3 - стоп '))

    if text == 1:
        name,surname =input('Введите имя и фамилию контакта ').title().split()
        pers = (surname,name)

        if pers in phonebook:
            print('Такой контакт уже есть')

        else:
            num =int(input('Теперь введите номер '))
            phonebook[(surname,name)] = num
            print(phonebook)

    elif text == 2:
        find_key =input('Введите фамилию контака ').title()
        found_contacts = [i for i, v in phonebook.items() if find_key.lower() == i[0].lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact, phonebook[contact])
        else:
            print('Такого контакта нет')

    elif text == 3:
        print('BB')
        break
