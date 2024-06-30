from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
quantity = int(input('Пивет, Манюня Любимая, сколько паролей хочешь сгенерировать? (напиши число)'))
lens = int(input('Какой длины должен быть пароль для моей принцессы? (напиши число)'))
digitstrue = input('Включать ли в пароль цифры от 0 до 9? ("дя" или "ни")')
uppercasetrue = input('Включать ли в пароль прописные буквы? ("дя" или "ни")')
lowercasetrue = input('Включать ли в пароль строчные буквы? ("дя" или "ни")')
punctuationtrue = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ("дя" или "ни")')
if digitstrue.lower() == 'дя':
    chars=chars+digits
if lowercasetrue.lower() == 'дя':
    chars=chars+lowercase_letters
if uppercasetrue.lower() == 'дя':
    chars=chars+uppercase_letters
if punctuationtrue.lower() == 'дя':
    chars=chars+punctuation
print(f'Вот твои {quantity} кокет пароля')
for i in range(quantity):
    password = ''
    for j in range(lens):
        password += choice(chars)
    print(password, sep = '\n')