def mean(a, b):
    try:
        a = int(a)
        b = int(b)

        mean_numbers = [a, b]
        d = len(mean_numbers)
        result_mean = (a + b) / d
        return float(result_mean)

    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
