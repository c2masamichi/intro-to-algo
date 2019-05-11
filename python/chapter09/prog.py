import random


def minimum(a):
    minv = a[0]
    for i in range(1, len(a)):
        if minv > a[i]:
            minv = a[i]
    return minv


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def randomized_partition(a, p, r):
    i = random.randint(p, r)
    a[r], a[i] = a[r], a[i]
    return partition(a, p, r)


def randomized_select(a, p, r, i):
    if p == r:
        return a[p]
    q = randomized_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return randomized_select(a, p, q - 1, i)
    else:
        return randomized_select(a, q + 1, r, i - k)
