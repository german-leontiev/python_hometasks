print('Задача 5. Недоделка')

# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители.
# У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.

# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку и выводит, победил он или проиграл.
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

# Правила игры «Угадай число»:
# программа запрашивает у пользователя число до тех пор, пока он не угадает загаданное.

# Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».


def rock_paper_scissors():
  print('«Камень, ножницы, бумага»')
  choice =input('Введите Камень, ножницы, или бумага: ')
  if choice == 'Камень' or choice == 'камень':
      print('Ничья')
  elif choice == 'Бумага' or choice == 'бумага':
      print('Вы выйграли')
  elif choice == 'Ножницы' or choice == 'ножницы':
      print('Вы проиграли')
  else:
      print('Неправильный ввод')
      rock_paper_scissors()




def guess_the_number():
  print('«Угадай число»')
  quest = 5
  attempts = 0
  num =int(input('Введите число: '))
  while num:
    if num < quest:
        attempts += 1
        num =int(input('Число меньше, чем нужно. Попробуйте ещё раз! '))
    elif num > quest:
        attempts += 1
        num =int(input('Число больше, чем нужно. Попробуйте ещё раз! '))
    else:
        attempts += 1
        print('Вы угадали! Число попыток: ',attempts)
        break
    main_menu()
    #скопировал свою же задачу



def main_menu():
  game =int(input('Во что хотите сыграть? (1 - Камень, ножницы, бумага),(2 - Угадай число)'))
  if game == 1:
      rock_paper_scissors()
  elif game == 2:
      guess_the_number()
  else:
     print('Неправильный ввод')
     main_menu()
  



main_menu()
