greeting = input('Приветствие: ')

if greeting.lower() == 'здравствуйте':
    print('$0')
elif greeting.lower()[0] == 'з':
    print('$20')
else:
    print('$100')
