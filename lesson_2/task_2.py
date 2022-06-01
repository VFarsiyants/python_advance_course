"""
Инкапсулировать оба параметра (название и цену) товара родительского класса. 
Убедиться, что при сохранении текущей логики работы программы будет 
сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким 
образом, чтобы получить доступ к защищенным переменным. Результат выполнения 
заданий 1 и 2 должен быть идентичным. 
"""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # получение защищенных переменных через геттеры
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    # переопределяем получение аргументов, так что проверять их
    # в составе защищенных
    def __getattr__(self, name: str):
        for attr in self.__dict__.keys():
            if name in attr:
                return self.__dict__[attr]
        super().__getattr__(name)


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'Название товара {self.name}\t цена товара {self.price} ₽')


itemPC = ItemDiscountReport('Настольный ПК', 49999.00)
itemPC.get_parent_data()
