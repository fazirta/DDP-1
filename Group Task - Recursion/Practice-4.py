def maximum_value(a: list[int]):
    if len(a) == 1:
        return a[0]
    else:
        if a[0] > a[1]:
            return maximum_value([a[0]] + a[2:])
        else:
            return maximum_value(a[1:])
