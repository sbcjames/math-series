def fibonacci(n):
  if n <= 0:
    return 0

  elif n == 1:
    return 0

  elif n == 2:
    return 1

  else:
    return fibonacci(n-1)+fibonacci(n-2)    

def lucas(nth):
  if nth == 0:
    return 2
  elif nth == 1:
    return 1
  elif nth == 2:
    return 3
  else:
    return lucas(nth-1)+lucas(nth-2)

