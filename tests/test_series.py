from math_series.math_series import fibonacci
from math_series.math_series import lucas
from math_series.math_series import sum_series

def test_import():
  assert fibonacci

def test_fibonacci_1():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_2():
  actual = fibonacci(1)
  expected = 0
  assert actual == expected

def test_fibonacci_3():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_4():
  actual = fibonacci(9)
  expected = 21
  assert actual == expected

def test_lucas_1():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_2():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_3():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_4():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lucas_5():
  actual = lucas(4)
  expected = 7
  assert actual == expected

