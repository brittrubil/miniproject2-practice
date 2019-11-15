def zscore(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = float((a - b) / c)
        return float(format(d, '.3f'))
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
