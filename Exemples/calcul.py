def main():
    print("Programme principal")
def addition(a : int, b : int):
    """
    Docstring for addition
    
    :param a: int
    :param b: int
    """
    return a + b
def soustraction(a : int, b : int):
    """
    Docstring for soustraction
    
    :param a: int
    :param b: int
    """
    return a - b
def multiplication(a : int, b : int):
    """
    Docstring for multiplication
    
    :param a: int
    :param b: int
    """
    return a * b
def division(a : int, b : int):
    """
    Docstring for division
    
    :param a: int
    :param b: int
    """
    if b == 0:
        raise ValueError("Division par 0 non autorisée")
    else:
        return a / b

if __name__ == "__main__":
    main()