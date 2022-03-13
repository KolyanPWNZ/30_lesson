from abc import ABC, abstractmethod


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
        self.items = set()
        # Добавление объекта в словарь (БД)
        Catalog.__catalog_list[Catalog.__id_catalog] = self

    @property
    def id(self):
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
                # ----------------------------
                # А как здесь может оказаться каталог?
                # перебираем же товары
                # ----------------------------
                out += 'Каталог ' + str(unit.id) + ' ' + str(unit.title) + '\n'
            elif type(unit) == Item:
                out += 'Товар/услуга ' + str(unit.id) + ' ' + str(unit.title) + '\n'
            else:
                print('Ошибка! Случайный объект, неверного формата!')
                # Можно вызвать исключение
        return out

    # ----------------------------
    # Думаю здесь больше бы подошло название метода get_new_catalog, иначе неочевидно, что будет возвращаться каталог
    # И подобное, стоит отправлять в классы интерфейсов
    # ----------------------------
    @staticmethod
    def create():
        # Запрос входной инофрмации у администратора для создания нового каталога
        # Для примера используется Input
        # Можно реализовать проверку входных данных
        title = input('Введите оглавление каталога: ')
        descr = input('Введите описание каталога: ')
        return Catalog(descr, title)

    # ----------------------------
    # Классное решение с меню, но думаю не хватает напечатать все пункты перед запросом номеров
    # И думаю, стоило бы расписать геттеры для полей, меню бы это разгрузило и проще было бы взаимодействовать с полями
    # И в сеттерах можно было валидировать сами данные
    # ----------------------------
    @staticmethod
    def change():
        # Здесь идет реализация внесения изменений в каталог
        # Для примера диалог реализован через print input
        # 0 - выход из меню редактирования
        # 1 - Показать все каталоги
        # 2 - Показать все итемы каталога
        # 3 - Перейти в каталог
        # 4 - Добавить Catalog в текущий каталог
        # 5 - Удалить Catalog из текущего каталога
        # 6 - Добавить Item в текущий каталог
        # 7 - Удалить Item из текущего каталога
        # 8 - Установить цену для Item
        # 9 - Изменить оглавление и описание каталога
        command = -1
        current_id = 0
        while command != 0:
            command = int(input('Введите номер команды: '))
            if command == 1:
                for unit in Catalog.__catalog_list.values():
                    print(unit.id, unit.title)
            elif command == 2:
                # Проверка на наличие id в словаре не проверяется
                # Предполагается, что выбор будет осуществляться из предложенных значений
                if current_id > 0:
                    for unit in Catalog.__catalog_list.get(current_id).items:
                        if type(unit) == Catalog:
                            print('Каталог', end=' ')
                        else:
                            print('Продукт', end=' ')
                        print(unit.id, unit.title)
            elif command == 3:
                current_id = int(input('Введите id каталога: '))
            elif command == 4:
                if current_id > 0:
                    Catalog.__catalog_list.get(current_id).items.add(
                        Catalog.__catalog_list.get(int(input('Введите id каталога: '))))
                else:
                    Catalog.create()
            elif command == 5:
                if current_id > 0:
                    Catalog.__catalog_list.get(current_id).items.remove(
                        Catalog.__catalog_list.get(int(input('Введите id каталога: '))))
                # Удаление каталога из словаря (БД) не предполагается
            elif command == 6:
                item_id = int(input('Введите id продукта: '))
                if not item_id in Catalog.__item_list:
                    # Предполагается, что итем существует, проверка не делается
                    Catalog.__item_list[item_id] = Offer(
                        Item.return_obj(item_id, float(input('Введите цену продукта: '))))
                if current_id > 0:
                    Catalog.__catalog_list.get(current_id).items.add(Catalog.__item_list.get(item_id).item)
            elif command == 7:
                if current_id > 0:
                    Catalog.__catalog_list.get(current_id).items.remove(
                        Catalog.__item_list.get(int(input('Введите id продукта: ')).item))
            elif command == 8:
                for unit in Catalog.__item_list.values():
                    print(unit.item.id, unit.item.title, 'цена', unit.price)
                Catalog.__item_list[int(input('Введите id продукта: '))].price = float(input('Введите цену продукта: '))
            elif command == 9:
                if current_id > 0:
                    Catalog.__catalog_list[current_id].title = input('Введите оглавление каталога: ')
                    Catalog.__catalog_list[current_id].description = input('Введите описание каталога: ')


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

    # ----------------------------
    # аналогично как с каталогами
    # Или ты реализовывал универсальные методы (судя по названиям), чтобы использовать в интерфейсе?
    # ----------------------------
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
        # Здесь идет реализация внесения изменений в итем
        # Для примера диалог реализован через print input
        # 0 - выход из меню редактирования
        # 1 - Показать все итемы
        # 9 - Изменить оглавление и описание итема
        command = -1
        while command != 0:
            command = int(input('Введите номер команды: '))
            if command == 1:
                for unit in Catalog.__catalog_list.values():
                    print(unit.id, unit.title)
            elif command == 9:
                item_id = int(input('Введите id продукта: '))
                Item.__item_list[item_id].title = input('Введите оглавление продукта: ')
                Item.__item_list[item_id].description = input('Введите описание продукта: ')


class Offer:

    def __init__(self, item: Item, price: float):
        self.__item = item
        self.price = price

    @property
    def item(self):
        return self.__item
