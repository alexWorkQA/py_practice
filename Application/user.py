class User:
    def __init__(self, name, id, email):
        self.__name = name
        self.__id = id
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name = name
        else:
            raise EnvironmentError






