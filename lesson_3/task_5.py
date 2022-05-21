"""
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором 
списке часть строковых значений (выбирается случайно) заменить на значения типа 
345example (в обратном порядке, число и строка). Реализовать функцию поиска 
определенных подстрок в файле по следующим условиям: вывод первого вхождения, 
вывод всех вхождений. Реализовать функцию замену всех найденных подстрок на 
новое значение и вывод измененных строк.
"""
import os


def write_file(filename):
    if filename in os.listdir():
        print(f'файл {filename} уже существует')
    keys = (key for key in ['345example', '345example12wong', 'monkey', 'lu'])
    vals = (val for val in [12, 92, 40, 37])
    with open(filename, 'w', encoding='utf-8') as f:
        for key, val in zip(keys, vals):
            f.write(f'{key}{val}\n')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.replace('\n', ''))

def search(filename, query, replace=False, replace_value='', first_hit=True):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.readlines()
        for i in range(len(content)):
            if query in content[i]:
                print(f'Найдено вхождение: {query}')
                if replace:
                    if first_hit:
                        content[i] = content[i].replace(query, replace_value, 1)
                    else:
                        content[i] = content[i].replace(query, replace_value)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(content)


if __name__ == '__main__':
    test_filename = 'test'
    write_file(test_filename)
    search(test_filename, '345example', replace=True, replace_value='example', first_hit=False)
    print('*' * 80)
    read_file(test_filename)
