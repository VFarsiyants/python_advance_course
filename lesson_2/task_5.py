"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний 
класс ItemDiscountReport на два класса. Инициализировать классы необязательно. 
Внутри каждого поместить функцию get_info, которая в первом классе будет 
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов 
каждой из функции get_info.
"""
from abc import ABC, abstractmethod


class ItemDiscount(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # у создаваемых экземпляров должен быть метод get_info
    @abstractmethod
    def get_info(self):
        pass
    

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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')

    def __str__(self):
        return f'{self.name} - {round(self.price * (1 - self.discount), 2)}'


class ItemDiscountReportPrice(ItemDiscount):
    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')

    def get_info(self):
        return self.price


class ItemDiscountReportName(ItemDiscount):
    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')

    def get_info(self):
        return self.name


itemPCprice = ItemDiscountReportPrice('Настольный ПК', 49999.00)
itemPCname = ItemDiscountReportName('Настольный ПК', 49999.00)

objects_list = [itemPCprice, itemPCname]

# проверяем множество форм метода у экземплеров разных классов
# возвращающего разные результаты
for obj in objects_list:
    print(obj.get_info())
