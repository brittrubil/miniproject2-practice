def standardscore(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = (a - b) / c
        return float(d)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
