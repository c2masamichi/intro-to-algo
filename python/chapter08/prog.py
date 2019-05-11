def counting_sort(a, b, k):
    c = [0] * (k+1)
    for j in range(len(a)):
        c[a[j]] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1


def counting_sort_by_digit(a, d):
    b = [0] * len(a)
    k = 10
    div = 10 ** (d-1)
    c = [0] * k
    for j in range(len(a)):
        r = (a[j] // div) % 10
        c[r] += 1
    for i in range(1, k):
        c[i] += c[i-1]
    for j in range(len(a) - 1, -1, -1):
        r = (a[j] // div) % 10
        b[c[r] - 1] = a[j]
        c[r] -= 1
    return b


def radix_sort(a, d):
    for i in range(1, d+1):
        a = counting_sort_by_digit(a, i)
    return a


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key


def bucket_sort(a):
    n = len(a)
    b = [[] for i in range(n)]
    for i in range(n):
        b[int(n * a[i])].append(a[i])
    for i in range(n):
        insertion_sort(b[i])
    c = []
    for i in range(n):
        c.extend(b[i])
    return c
