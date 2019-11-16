def sample_proportion(a, b, c):
    try:
        count = int(a)
        nobs = int(b)
        value = int(c)
        stat, pval = proportions_ztest(count, nobs, value)
        return float(format(pval, '.2f'))

    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
