from statistics import pstdev


def population_deviation(a, b , c, d, e, f):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    f = float(f)

    num_list = [a, b, c, d, e, f]
    return round(pstdev(num_list), 2)
