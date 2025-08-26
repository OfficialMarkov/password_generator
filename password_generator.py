from random import *

def is_valid(s):
    return str(s).isdigit() and int(s) >= 1

def generate_password(len_password, chars, count_password):
    if not is_valid(len_password) or not is_valid(count_password):
        print('А может все таки введем число больше 0? \n')
        return []
    return [''.join(choice(chars) for _ in range(len_password)) for _ in range(count_password)]

def evaluate_password_strength(password):
    score = 0
    if any(c.isdigit() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in punctuation for c in password): score += 1
    return ['Слабый', 'Средний', 'Надежный', 'Очень надежный'][score - 1]

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'\
    
while True:

    len_password = int(input('Сколько должно быть символов в пароле? \n'))
    count_password = int(input('Сколько должно быть паролей сгенерировано? \n'))
    if not is_valid(len_password) or not is_valid(count_password):
        print('Пожалуйста, введите положительные числа. \n')
        continue

    chars = ''
    if input('Должен ли пароль содержать строчные буквы? \n').lower() == 'да':
        chars += lowercase_letters
    if input('Должен ли пароль содержать цифры? \n').lower() == 'да':
        chars += digits
    if input('Должен ли пароль содержать специальные символы? \n').lower() == 'да':
        chars += punctuation
    if input('Должен ли пароль содержать прописные буквы? \n').lower() == 'да':
        chars += uppercase_letters
    if input('Нужно исключить неоднозначные символы (il1Lo0O)? \n').lower() == 'да':
        chars = ''.join(c for c in chars if c not in 'il1Lo0O')
    if not chars:
        print('Ошибка! Вы не выбрали ни одну категорию символов. Пароль не может быть создан.')
        continue
    
    passwords = generate_password(len_password,chars, count_password)
    
    print('\nСгенерированные пароли:')
    for password in passwords:
        print(password)
        print(f'Оценка вашего пароля - {evaluate_password_strength(password)}')
    if input('Хотите сгенерировать новый пароль? \n').lower() != 'да':
        print('Спасибо за использование генератора паролей!')
        break
     