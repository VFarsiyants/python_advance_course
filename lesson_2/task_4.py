"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться 
в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора 
дочернего класса (метод __init__, в который должна передаваться переменная — 
скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна 
пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы 
все работало корректно, не забудьте инициализировать дочерний и родительский 
классы (вторая и третья строка после объявления дочернего класса). 
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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')

    def __str__(self):
        return f'{self.name} - {round(self.price * (1 - self.discount), 2)}'


itemPC = ItemDiscountReport('Настольный ПК', 49999.00, 0.2)
itemPC.get_parent_data()

print(itemPC)
