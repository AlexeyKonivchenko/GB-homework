price_list = [57.8, 65.09, 79.15, 100.22, 54, 33.10, 25.05, 199.99, 81, 19.90]


print('Задание "А"')
for p in price_list:
    print(f'{int(p)} руб. {int(p * 100 % 100): 02} коп.', end=' ,')


print('\n\nЗадание "B"')
print(f'прайс лист: {price_list} id:{id(price_list)}')
price_list.sort()
print(f'После сортировки : {price_list} id:{id(price_list)}')


print('\n\nЗадание "C"')
sor_price = sorted(price_list, reverse=True)
print(f'Новый прайс по убыванию: {sor_price} id:{id(sor_price)}')


print('\n\nЗадание "D"')
print(price_list[-5:])
