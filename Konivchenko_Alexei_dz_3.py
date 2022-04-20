for n in range(1, 101):
    if n % 10 == 1:
        print(n, 'процент')
    elif 20 > n > 10 or n % 10 in [0, 5, 6, 7, 8, 9]:
        print(n, 'процентов')
    else:
        print(n, 'процента')