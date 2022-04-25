duration = int(input('Введите время в секундах: '))
hours = duration // 3600
remainder_secs = duration % 3600
minutes = remainder_secs // 60
remainder_secs = remainder_secs % 60
days = hours // 24
hours = hours % 24

if duration >= 3600:
    print(days, 'д', hours, 'ч', minutes, 'мин', remainder_secs, 'сек')
elif duration <= 3600:
    print(minutes, 'мин', remainder_secs, 'сек')
