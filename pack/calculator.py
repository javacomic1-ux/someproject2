def add(a, b):
    result = a + b
    print("Add:", result)
    return result

def subtract(a, b):
    result = a - b
    print("Subtract:", result)
    return result

def multiply(a, b):
    result = a * b
    print("Multiply:", result)
    return result

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    result = a / b
    print("Divide:", result)
    return result