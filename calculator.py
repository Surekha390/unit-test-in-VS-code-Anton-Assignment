def add_numbers(a, b):   # This is the function we are going to test
    return a + b

def mul_numbers(a, b):
    return a * b

def div_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def subtraction(d, e):
    return d - e