def correlation_coefficient(a):
    try:
        a = float(a)
        return float(stats.pearsonr(a))
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
