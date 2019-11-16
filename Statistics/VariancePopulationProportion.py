

def populationproportion(a, b):
    try:
        a = int(a)
        b = int(b)
        c = ((a ** 2) / b) ** 2
        return c
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")