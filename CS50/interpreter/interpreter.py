expr = input('Expression: ')

try:
    print(float(eval(expr)))
except ZeroDivisionError:
    pass