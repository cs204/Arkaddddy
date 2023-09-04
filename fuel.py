while True:
    try:
        fraction = input('Дробь: ')
        nums = fraction.split('/')
        x = int(nums[0])
        y = int(nums[1])
        tank = round(x / y * 100)
        if tank <= 1:
            print('E')
            break
        elif tank >= 99:
            print('F')
            break
        else:
            print(f'{tank}%')
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
