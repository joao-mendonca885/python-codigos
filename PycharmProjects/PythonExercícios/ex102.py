def fat(n, show):
    fatorial = 1
    for c in range(n, 0, -1):
        fatorial = fatorial * c
        if show: 
            if c > 1: print(f"{c} x ", end="")
            else: print(f"{1} = ", end="")
    return fatorial


print(fat(5, False))
