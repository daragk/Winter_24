class Person:
    def __init__(self, surname, name, otchestvo):
        self.surname = surname
        self.name = name
        self.otchestvo = otchestvo

    def __str__(self):
        return (self.surname + self.name + self.otchestvo)[::-1]

p = Person('John', 'Doe', 'Vasilyevich')
print(p)