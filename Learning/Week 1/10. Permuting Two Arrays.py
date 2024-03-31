def twoArrays(k, A, B):

    permute_a = sorted(A)
    permute_b = sorted(B, reverse=True)

    for i in range(0, len(permute_a) - 1):
        if permute_a[i] + permute_b[i] < k:
            return "NO"

    return "YES"


twoArrays(1,[0,1],[0,2])