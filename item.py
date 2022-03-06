from abc import ABC, abstractmethod

from matplotlib.pyplot import cla

class IChange(ABC):

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def change():
        pass

class ISurfing(ABC):

    @abstractmethod
    def show_items(id):
        pass

class Catalog(ISurfing, IChange):

    __id_catalog = 0
    __item_list = dict()
    __catalog_list = dict()

    def __init__(self, description: str = None, title: str = None):
        Catalog.__id_catalog += 1
        self.__id = Catalog.__id_catalog
        self.description = description
        self.title = title
        self.items = list()
        # Добавление объекта в словарь (БД)
        Catalog.__catalog_list[Catalog.__id_catalog] = self

    @property
    def ip(self):
        return self.__id

    @staticmethod
    def get_price(item):
        # Выдача цены
        return Catalog.__item_list[item].price

    @staticmethod
    def show_items(id):
        # Вывод информации о каталоге, формат зависит от реазизации
        # Проверка не выполняется
        out = ''
        for unit in Catalog.__catalog_list[id].items:
            if type(unit) == Catalog:
                out += 'Каталог ' + str(unit.id) + ' ' + str(unit.title) + '\n'
            elif type(unit) == Item:
                out += 'Товар/услуга ' + str(unit.id) + ' ' + str(unit.title) + '\n'
            else:
                print('Ошибка! Случайный объект, неверного формата!')
                # Можно вызвать исключение
        return out

    @staticmethod
    def create():
        # Запрос входной инофрмации у администратора для создания нового каталога
        # Для примера используется Input
        # Можно реализовать проверку входных данных
        title = input('Введите оглавление каталога: ')
        descr = input('Введите описание каталога: ')
        return Catalog(descr, title)

    @staticmethod
    def change():
        # Здесь идет реализация внесения изменений в каталог
        # Для примера диалог реализован через print input
        # 0 - выход из меню редактирования
        # 1 - Показать все каталоги
        # 2 - Показать все итемы
        # 3 - Перейти в каталог
        # 4 - Добавить Catalog в текущий каталог
        # 5 - Удалить Catalog из текущего каталога
        # 6 - Добавить Item в текущий каталог
        # 7 - Удалить Item из текущего каталога
        # 8 - Установить цену для Item
        # 9 - Изменить оглавление и описание каталога
        command = -1
        while command != 0:
            command = int(input('Введите номер команды: '))


class Item(IChange):

    __id_item = 0
    __item_list = dict()

    def __init__(self, description: str = None, title: str = None):
        Item.__id_item += 1
        self.__id = Item.__id_item
        self.description = description
        self.title = title
        # Добавление объекта в словарь (БД)
        Item.__item_list[Item.__id_item] = self

    @property
    def id(self):
        return self.__id

    @staticmethod
    def return_obj(item):
        # Защита от неверных данных не реализована, реализовывать тут
        return Item.__item_list[item]
    
    @staticmethod
    def create():
        # Запрос входной инофрмации у администратора для создания нового итема
        # Для примера используется Input
        # Можно реализовать проверку входных данных
        title = input('Введите оглавление продукта/услуги: ')
        descr = input('Введите описание продукта/услуги: ')
        return Item(descr, title)

    @staticmethod
    def change():
        # Здесь идет реализация внесения изменений в каталог
        # Для примера диалог реализован через print input
        # 0 - выход из меню редактирования
        # 1 - Показать все итемы
        # 9 - Изменить оглавление и описание каталога
        command = -1
        while command != 0:
            command = int(input('Введите номер команды: '))

class Offer:

    def __init__(self, item: Item, price: float):
        self.__item = item
        self.price = price
    
    @property
    def item(self):
        return self.__item
