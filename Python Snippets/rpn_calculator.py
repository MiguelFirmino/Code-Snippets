def divisionWithTest(dividend, divisor):
  if divisor == 0:
    return None
  else:
    return dividend / divisor

def expression(lhs, rhs, operation):
  if operation == "+":
    return lhs + rhs
  elif operation == "-":
    return lhs - rhs
  elif operation == "*":
    return lhs * rhs
  elif operation == "/":
    return divisionWithTest(lhs, rhs)

def reversePolishCalc(expressionText):
  '''
  receives math expression as a string written in
  reverse polish nonation and returns the result
  '''
  lhs = rhs = result = None

  for char in expressionText.split():
    if char.isnumeric():
      if not lhs:
        lhs = int(char)
      else:
        rhs = int(char)
    elif char in "+-*/" and rhs != None:
      # "pushes" the result to left-hand side so following
      # operations are done with it
      lhs = result = expression(lhs, rhs, char)
      rhs = None

  return result