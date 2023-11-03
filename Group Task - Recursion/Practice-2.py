def length(l: list):
    if l == []:
        return 0
    else:
        return 1 + length(l[:-1])
