def pvalue(a, b, c, d):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        pValue_list = [a, b, c, d]
        e = len(pValue_list)
        f = e - 1
        squareChi = float(((a - c) ** 2) / c) + (((b - d) ** 2) / d)
        return squareChi
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")


