def power(a: int, b: int):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
