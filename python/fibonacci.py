from pyparsing import RecursiveGrammarException


def fibonacci(n):
  a = 0
  b = 1
  sum = 0

  for i in range(1, n):
    sum = a + b
    a = b
    b = sum

  return sum
