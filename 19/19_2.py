class Fibbonacci:
  def __init__(self):
    self.value = 0
    self.predid = 1
  def __iter__(self):
    return self
  def __next__(self):
    fib = self.value + self.predid
    self.predid = self.value
    self.value = fib
    return fib

s = Fibbonacci()
for i in range(10):
  print(next(s))