class Person:
    def __init__(self, name):
        self.name = name
        self.drinks_spends = 0
        self.bakery_spends = 0
        self.orders = {}
    def zakaz(self, drink, bakery, cafe):
        drink = drink.capitalize()
        bakery = bakery.capitalize()
        print(f"I'll get a {drink} with {bakery}")

        self.drinks_spends += cafe.menu_drinks.get(drink)
        self.bakery_spends += cafe.menu_bak.get(bakery)
        if drink not in self.orders:
            self.orders[drink] = 1
        else:
            self.orders[drink] += 1
        if bakery not in self.orders:
            self.orders[bakery] = 1
        else:
            self.orders[bakery] += 1

    def info(self):
        print(f"Drinks spends equel {self.drinks_spends}, bakery spends equel {self.bakery_spends}")
        print(f"Your favourite item is {max(self.orders, key=lambda x: self.orders[x])}")

class Menu:
    def __init__(self, name):
        self.name = name
        #self.price = price
        self.menu_bak = {}
        self.menu_drinks = {}
    def show_menu(self, m_type):
        if m_type == "drinks":
            for drink in self.menu_drinks:
                print(f'{drink} is for {self.menu_drinks[drink]}')
        elif m_type == "bakery":
            for bak in self.menu_bak:
                print(f'{bak} is for {self.menu_bak[bak]}')


vasya = Person("Vasya")
caf = Menu('The Best coffee')
caf.menu_drinks = {'Americano': 100, 'Latte': 150, 'Raf': 230, 'Ice Latte': 170, 'Tea': 80}
caf.menu_bak = {'Cookies': 99, 'Tarts': 119, 'Sandwichies': 179, 'Cheesecakes': 108}

caf.show_menu('bakery')
print()
caf.show_menu('drinks')
print()
vasya.zakaz('tea', 'Cookies', caf)
vasya.zakaz('Latte', 'Cookies', caf)
print()
vasya.info()
