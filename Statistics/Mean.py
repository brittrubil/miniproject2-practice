def mean(a, b):
    try:
        a = int(a)
        b = int(b)
        c = int(a + b)
        return c / 2

    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
