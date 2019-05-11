def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = []
    right = []
    for i in range(n1):
        left.append(a[p+i])
    for j in range(n2):
        right.append(a[q+j+1])
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
