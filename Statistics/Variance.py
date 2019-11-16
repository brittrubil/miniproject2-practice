from statistics import pvariance


def variance(a, b, c, d, e, f, g, h):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        g = float(g)
        h = float(h)
        num_list = [a, b, c, d, e, f, g, h]
        return pvariance(num_list)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
