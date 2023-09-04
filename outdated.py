months = ["январь", "февраль", "март", "апрель", "май",
          "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

while True:
    try:
        date = input('Дата: ')
        if '.' in date:
            date_list = date.split('.')
        else:
            date_list = date.split(' ')
        if date_list[1].lower() in months:
            month = months.index(date_list[1].lower()) + 1
        else:
            month = int(date_list[1])
        day = int(date_list[0])
        year = int(date_list[2])
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f'{year}-{month:02}-{day:02}')
            break
        pass
    except ValueError:
        pass
