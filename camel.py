string = input()
result = ''
for c in string:
    if c.isupper():
        result = result + '_' + c.lower()
    else:
        result += c
print(f'Верблюжий стиль: {result}')
