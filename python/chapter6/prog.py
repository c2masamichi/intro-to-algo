def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(a, i):
    heap_size = len(a) - 1
    l_index = left(i)
    r_index = right(i)
    if l_index <= heap_size and a[l_index] > a[i]:
        largest = l_index
    else:
        largest = i
    if r_index <= heap_size and a[r_index] > a[largest]:
        largest = r_index
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    length = len(a) - 1
    for i in range(length // 2, 0, -1):
        max_heapify(a, i)
