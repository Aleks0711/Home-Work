str_x = input('Ведите строку:')
if set(str_x).issubset({'0', '1'}):
    print('Yes')
elif set(str_x.rsplit('b')[-1]).issubset({'0', '1'}) and str_x.rsplit('b')[0] in ('', '0'):
    print('Yes')
else:
    print('No')

#Вывод
#Ведите строку:0b01001110
#Yes
