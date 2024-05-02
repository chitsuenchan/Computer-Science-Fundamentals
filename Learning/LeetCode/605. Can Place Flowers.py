def canPlaceFlowers(f,n) -> bool:
    if n == 0:
        return True

    if len(f) == 1:
        if f[0] == 0:
            return True
        else:
            return False

    for i in range(len(f)):
        if i == 0:
            if f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        elif i == len(f) - 1:
            if f[i - 1] == 0 and f[i] == 0:
                f[i] = 1
                n -= 1
        else:
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        if n == 0:
            return True
    return False

f = [1,0,0,0,1]
n = 2

print(canPlaceFlowers(f,n))