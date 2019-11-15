import statistics


def mode(a, b , c, d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    num_list = [a, b, c, d]
    return statistics.mode(num_list)