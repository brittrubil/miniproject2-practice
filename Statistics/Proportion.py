def proportion(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        ratio = a/b
        pro = c / ratio
        return pro
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
