# Задача 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать надёжный пароль. 
# Этот пароль должен состоять минимум из восьми символов, в нём должна быть хотя бы одна прописная буква и хотя бы три цифры. 
# Тогда он будет считаться надёжным.

# Напишите программу, которая запрашивает пароль у пользователя до тех пор, пока пароль не окажется надёжным. 
# Используется латиница.

# Пример:
# Придумайте пароль: qwerty
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!



while True:
    count = 0
    count_big = 0
    text =input('Придумайте пароль: ')
    if len(text) >= 8:
        for i in range(len(text)):
            if text[i].isdigit():
                count += 1
            if text[i].isupper():
                count_big +=1
        if count >= 3 and count_big >= 1:
            print('Это надёжный пароль!')
            break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
