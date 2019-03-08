def counting_sort(a, b, k):
    c = [0] * (k+1)
    for j in range(len(a)):
        c[a[j]] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]
        c[a[j]] -= 1
