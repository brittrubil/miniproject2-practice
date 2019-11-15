def median(a, b, c, d):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        num_list = [a, b, c, d]
        # Sort the list
        num_list.sort()
        # Finding the position of the median
        if len(num_list) % 2 == 0:
            first_median = num_list[len(num_list) // 2]
            second_median = num_list[len(num_list) // 2 - 1]
            result_median = (first_median + second_median) / 2
        else:
            result_median = num_list[len(num_list) // 2]
        return result_median
    except ZeroDivisionError:
        print("Error: Number Not Valid")
    except ValueError:
        print("Error: Only Numeric Values")
