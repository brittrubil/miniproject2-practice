def median(a, b , c, d):
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
        median = (first_median + second_median) / 2
    else:
        median = num_list[len(num_list) // 2]
    return median