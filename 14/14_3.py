def func(n):
  print('*' * n)
  n -= 1
  if n > 1:
    func(n)
  print('*' * n)
  return
func(6)