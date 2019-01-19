def f(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i >= 3:
        return f(i-1) + f(i-2)


print(f(1))

