"""
Создать два класса. Первый — родительский (ItemDiscount), должен содержать 
статическую информацию о товаре: название и цену. Второй — дочерний 
(ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую 
за отображение информации о товаре в одной строке вида (“{название товара} 
{цена товара}”). Создать экземпляры родительского класса и дочернего. 
Распечатать информацию о товаре.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')


itemPC = ItemDiscountReport('Настольный ПК', 49999.00)
itemPC.get_parent_data()
