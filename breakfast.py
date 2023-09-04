menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}
order_summ = 0.00

while True:
    try:
        item = input('Блюдо: ').lower()
        if item in menu:
            order_summ += menu[item]
    except EOFError:
        print(f'\nСумма: {order_summ:.2f}')
        break
