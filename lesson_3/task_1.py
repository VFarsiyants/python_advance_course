"""
Написать программу, которая будет содержать функцию для получения имени файла 
из полного пути до него. При вызове функции в качестве аргумента должно 
передаваться путь и имя файла с расширением. В функции необходимо реализовать 
поиск имени файла (с расширением), а затем «выделение» имени файла (без 
расширения). Расширений может быть несколько (например testfile.tar.gz).
"""
import os


def get_filename(file_path):
    file_name = os.path.basename(file_path)
    return file_name.split('.')[0]


if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.abspath(__file__))
    test_path = os.path.join(cur_path, 'testfile.tar.gz')
    print(get_filename(test_path))
