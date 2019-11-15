from statistics import stdev


def deviation(a, b , c, d, e):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)

    num_list = [a, b, c, d, e]
    return round(stdev(num_list), 2)
