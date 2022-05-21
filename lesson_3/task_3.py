"""
Создать два списка с различным количеством элементов. В первом должны быть 
записаны ключи, во втором — значения. Необходимо написать функцию, создающую из 
данных ключей и значений словарь. Если ключу не хватает значения, в словаре 
для него должно сохраняться значение None. Если есть  значения, которым не 
хватило ключей, их необходимо отбросить. 
"""
from itertools import zip_longest


keys = ['жук', 'vika', 'red', 'dog']
values = [1233, 'nol', 153254]

len_dict = len(keys)
if len_dict < len(values):
    values = values[0:len_dict]

result = {}

for key, val in zip_longest(keys, values, fillvalue=None):
    result[key] = val

print(result)
