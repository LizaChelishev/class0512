class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
