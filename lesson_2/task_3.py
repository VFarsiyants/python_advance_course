"""
Реализовать возможность переустановки значения цены товара в родительском 
классе. Проверить, распечатать информацию о товаре.
"""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # получение защищенных переменных через геттеры (Ванильно по методичке)
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    # установка значений через setter (Ванильно по методичке)
    def set_name(self, value):
        self.__name = value

    def set_price(self, value):
        self.__price = value

    # переопределяем получение аргументов, так что проверять их
    # в составе защищенных
    def __getattr__(self, name: str):
        for attr in self.__dict__.keys():
            if name in attr:
                return self.__dict__[attr]
        super().__getattribute__(name)

    # Переопределение через setattr для изменения защищенных переменных
    def __setattr__(self, name, value):
        for attr in self.__dict__.keys():
            if name in attr:
                self.__dict__[attr] = value
                return
        return super().__setattr__(name, value)


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')


itemPC = ItemDiscountReport('Настольный ПК', 49999.00)
itemPC.get_parent_data()

# Проверяем изменение имени и цены
itemPC.name = 'Измененный настольный ПК'
itemPC.price = 59999.00
print(itemPC.__dict__)
print(itemPC._ItemDiscount__name)
print(itemPC._ItemDiscount__price)
