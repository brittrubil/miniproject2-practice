def proportion(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        ratio = a/b
        pro = c / ratio
        return float(format(pro, '.2f'))
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
