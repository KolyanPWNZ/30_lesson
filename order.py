from abc import ABC, abstractmethod
from  enum import Enum
from datetime import datetime
from order import Item, Catalog # Это видимо опечатка



# Перечисление статуса заказа
class OrderStatus(Enum):
    ACTIVE = 0
    PAID = 1
    EXPIRED = 2

class IOrder(ABC):

    @abstractmethod
    def add_item(user_id, item_id):
        pass

    @abstractmethod
    def delete_item(user_id, item_id):
        pass

    @abstractmethod
    def clear_order(user_id):
        pass

    @abstractmethod
    def pay_order(user_id):
        pass

class Order(IOrder):

    __id_order = 0
    __orders = dict()

    def __init__(self):
        Order.__id_order += 1
        self.__id = Order.__id_order
        self.__status = OrderStatus.ACTIVE
        self.__time = datetime.now()
        self.__order_list = dict()

    def __add(self, item):
        # Проверка наличия позиции в списке заказа
        if not item in self.__order_list:
            self.__order_list[item] = OrderItem(item, Catalog.get_price(item))
        # Добавление количества в спеисок заказа
        self.__order_list[item].count += 1

    def __delete(self, item):
        # Проверка наличия позиции в списке заказа
        if item in self.__order_list:
            # Удаление заказа
            self.__order_list.pop(item)

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self.__status

    @property
    def time(self):
        return self.__time

    @staticmethod
    def add_item(user_id, item_id):
        # Проверка существования и создания элемента словаря
        if not user_id in Order.__orders:
            Order.__orders[user_id] = dict()
            Order.__orders[user_id]['active'] = Order()
            Order.__orders[user_id]['paid'] = list()
        Order.__orders[user_id]['active'].__add(item_id)

    @staticmethod
    def delete_item(user_id, item_id):
        if user_id in Order.__orders:
            Order.__orders[user_id]['active'].__delete(item_id)

    @staticmethod        
    def clear_order(user_id):
        # Проверка существования и создания элемента словаря
        if not user_id in Order.__orders:
            Order.__orders[user_id] = dict()
            Order.__orders[user_id]['active'] = Order()
            Order.__orders[user_id]['paid'] = list()
        else:
            Order.__orders[user_id]['active'].__order_list = dict()

    @staticmethod
    def pay_order(user_id):
        # ----------------------------
        # "not" - здесь судя по всему лишний
        # ----------------------------
        if not user_id in Order.__orders:
            # Проверка статуса заказа (актуальность цен)
            if Order.__orders[user_id]['active'].__status == OrderStatus.ACTIVE:
                # Проверка на пустоту списка не проверяется!!!
                # Сюда вставляется код оплаты заказа
                # Перенос заказа в архив
                Order.__orders[user_id]['active'].__status = OrderStatus.PAID
                Order.__orders[user_id]['paid'].append(Order.__orders[user_id]['active'])
                Order.__orders[user_id]['active'] = Order()

class OrderItem:

    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.count = 0

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, id):
        self.__item = Item.return_obj(id)