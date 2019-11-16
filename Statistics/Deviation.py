from statistics import stdev


def deviation(a, b , c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        num_list = [a, b, c, d, e]
        return round(stdev(num_list), 2)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
