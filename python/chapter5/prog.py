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
