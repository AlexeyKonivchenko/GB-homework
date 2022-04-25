word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(word_list):
    if s.isdigit():
        word_list[i] = f'"{int(s):02d}"'
    elif s[i:].isdigit():
        word_list[i] = f'"{s[0]}{int(s[1:]):02d}'
        print(word_list[i], end=' ')
print(word_list)