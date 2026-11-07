def qs(arg):
    if len(arg) <= 1:
        return arg

    pivot = arg[len(arg) // 2]
    l = [x for x in arg if x < pivot]
    ser = [x for x in arg if x == pivot]
    r = [x for x in arg if x > pivot]

    return qs(l) + ser + qs(r)

primer = [10, 7, 8, 9, 1, 5, 7]
print(qs(primer))