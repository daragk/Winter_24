def low_reg(func):
    def wrapper():
        orig = func()
        modif = orig.lower()
        return modif
    return wrapper

@low_reg
def h():
  return 'ALOHA'

print(h())