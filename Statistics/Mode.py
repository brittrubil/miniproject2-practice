import statistics


def mode(a, b, c, d):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        num_list = [a, b, c, d]
        return statistics.mode(num_list)
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")