import random

class User:

    # Счетчик пользователей
    __id_counter = 0
    __users = dict()

    def __init__(self, name, surname):
        User.__id_counter += 1
        self.__id = User.__id_counter
        self.__phone = None
        self.__name = None
        self.__surname = None
        # Заполнение имен полей через методы свойств
        self.name = name
        self.surname = surname
        # Добавляем объект в словарь (БД)
        if self.name and self.surname:
            User.__users[self.id] = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # Проверка имени пользователя
        # Сюда вставляется код проверка, сейчас сделана заглушка
        if name:
            self.__name = name

    @property
    def surname(self):
        return self.__surname


    @surname.setter
    def surname(self, surname):
        # Проверка фамилия пользователя
        # Сюда вставляется код проверка, сейчас сделана заглушка
        if surname:
            self.__surname = surname        

    @property
    def id(self):
        return self.__id

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        key = ''
        for i in range(4):
            key += str(random.randint(0,9))
        # Отправляем код
        print(key)
        if input('Вам на телефон выслан код подтверждения:') == key:
            self.__phone = phone

     # Проверка существования пользователя в словаре (БД)
    @staticmethod
    def is_user_valid(id):
        return id in User.__users


class Admin(User):

    def __init__(self, name, surname):
        super().__init__(name,surname)

    def create_item():
        pass
    
    def create_catalog():
        pass

    def change_item():
        pass

    def change_catalog():
        pass
