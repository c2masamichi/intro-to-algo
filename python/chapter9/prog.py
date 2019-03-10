def minimum(a):
    minv = a[0]
    for i in range(1, len(a)):
        if minv > a[i]:
            minv = a[i]
    return minv
