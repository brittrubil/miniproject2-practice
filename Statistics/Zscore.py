def zscore(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = (a - b) / c
        return d
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
