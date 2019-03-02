from operator import itemgetter
import random


def sort_by_priority(a, p):
    pairs = list(zip(a, p))
    pairs.sort(key=itemgetter(1))
    for i in range(len(a)):
        a[i] = pairs[i][0]


def permute_by_sorting(a):
    n = len(a)
    p = [1] * n
    for i in range(n):
        p[i] = random.randint(1, n ** 3)
    sort_by_priority(a, p)


def randomize_in_place(a):
    n = len(a)
    for i in range(n):
        r = random.randint(i, n-1)
        a[i], a[r] = a[r], a[i]
