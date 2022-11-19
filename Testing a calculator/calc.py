def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y==0:
        raise ValueError('Can not divide by zero.')
    return x / y
