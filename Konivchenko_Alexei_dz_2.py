new_list_a = []
for i in range(1, 1001, 2):
    new_list_a.append(i ** 3)
print(new_list_a)


new_list_b = []
sum_digist = 0
for num in new_list_a:
    i = num
    while num != 0:
        sum_digist += num % 10
        num = num // 10
        if sum_digist % 7 == 0:
            new_list_b.append(i)
            sum_digist = 0
print(sum(new_list_b))

sum_cube = 0
for num in new_list_a:
    sum1 = 0
    i = num
    num += 17
    while num != 0:
        sum1 += num % 10
        num = num // 10
        if sum1 % 7 == 0:
            sum_cube += i + 17

print(sum_cube)
