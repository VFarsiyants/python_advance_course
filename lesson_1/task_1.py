"""
Вывести таблицу умножения в виде. 
1 x 1 = 1
1 x 2 = 2
..
1 x 10 = 10
— 
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N

Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
Между разделами вывести разделитель в виде 5 девисов 
"""
import sys
try:
    n = int(sys.argv[1])
except:
    print('Parameter N has not been provided')
    sys.exit(1)

for i in range(1, n+1):
    for k in range(1, 11):
        print(f'{i} * {k} = {i * k}')
    print('-----')
