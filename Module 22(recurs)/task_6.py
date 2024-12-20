# Задача 6. Глубокое копирование
# Что нужно сделать
# Вы сделали для заказчика структуру сайта по продаже телефонов:

# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iPhone',
#             'div': 'Купить',
#             'p': ‘Продать'
#         }
#     }
# }
# Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров. 
# Вы посчитали, что это лёгкая задача, и быстро принялись за работу. 

# Напишите программу, которая запрашивает у клиента, сколько будет сайтов, 
# а затем запрашивает название продукта и после каждого запроса выводит на экран активные сайты. 

# Условия: структуру сайта нужно описать один раз, копипасту никто не любит.

# Подсказка: используйте рекурсию.

# Пример:

# Сколько сайтов: 2

# Введите название продукта для нового сайта: iPhone

# Сайт для iPhone: 

# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам iPhone недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iPhone',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
# Введите название продукта для нового сайта: Samsung

# Сайт для iPhone: 

# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам iPhone недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iPhone',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }

# Сайт для Samsung: 
# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам Samsung недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на Samsung',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }

site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def create_site(phone_model):
    site = site_template.copy()
    site['html'] = site['html'].copy()
    site['html']['head'] = site['html']['head'].copy()
    site['html']['body'] = site['html']['body'].copy()
    
    site['html']['body']['h2'] = f'У нас самая низкая цена на {phone_model}'
    site['html']['head']['title'] = f'Куплю/продам {phone_model} недорого'
    
    return site

def main():
    number = int(input('Сколько сайтов: '))
    for i in range(number):
        phone_model = input(f'Введите название продукта для нового сайта: ')
        site = create_site(phone_model)
        print(f'Сайт для {phone_model}: \nsite = {site}\n')
main()

#ахуеть копии,жаль в скилбоксе об этом ни слова не было
