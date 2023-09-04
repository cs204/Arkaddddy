coins = 0
while coins < 50:
    print(f'Нужная сумма: {50 - coins}')
    coins += int(input('Вставьте монету: '))
print(f'Ваша сдача: {coins - 50}')
