class Person:
    def __init__(self, name, age):
        self.__age = age
        self._name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, other_age):
        if other_age in range(1,101):
            self.__age = other_age
        else:
            print('Invalid age')

    @age.getter
    def age(self):
        return self.__age

    @age.deleter
    def age(self):
        del self.__age


a = Person('ooo', 22)
a.age = 999
#print(a.age)
