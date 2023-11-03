def sum_digits(n: int):
    if n < 10:
        return n
    else:
        return int(str(n)[0]) + sum_digits(int(str(n)[1:]))
