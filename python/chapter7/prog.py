import random


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def randomized_partition(a, p, r):
    i = random.randint(p, r)
    a[r], a[i] = a[r], a[i]
    return partition(a, p, r)


def randomized_quicksort(a, p, r):
    if p < r:
        q = randomized_partition(a, p, r)
        randomized_quicksort(a, p, q - 1)
        randomized_quicksort(a, q + 1, r)
