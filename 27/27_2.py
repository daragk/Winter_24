class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  # def __getattribute__(self, attr):
  #   return object.__getattribute__(self, attr).capitalize()

  def __getattr__(self, attr): #работа с атрибутами, которых нет
    return f"total: {self.price * self.quantity}"

tovar = Item('tea', 99, 5)
print(tovar.total)
#print(tovar.name)