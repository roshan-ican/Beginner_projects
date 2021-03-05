def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """subtraact a function"""
    return x - y

def multiple(x, y):
    """Multiply a fuction"""
    return x * y

def divide(x, y):
    """Divide a function"""
    if y == 0:
        raise ValueError('can not divide with Zero!')
    return x / y