print('Карточки')
print()
card = int(input('Введите количество карточек: '))
card_summ = 0
for miss in range(1,card):
    card_summ +=int(input('Введите номер оставшейся карточки: '))
    card += miss
print('Номер пропавшей карточки: ', card - card_summ)