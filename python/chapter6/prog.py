def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(a, i, heap_size=None):
    if heap_size is None:
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
        max_heapify(a, largest, heap_size)


def build_max_heap(a):
    length = len(a) - 1
    for i in range(length // 2, 0, -1):
        max_heapify(a, i)


def heapsort(a):
    build_max_heap(a)
    length = len(a) - 1
    heap_size = length
    for i in range(length, 1, -1):
        a[1], a[i] = a[i], a[1]
        heap_size -= 1
        max_heapify(a, 1, heap_size)


def heap_maximum(a):
    return a[1]


def heap_extract_max(a):
    heap_size = len(a) - 1
    if heap_size < 1:
        raise Exception('Heap Underflow')
    maxv = a[1]
    a[1] = a.pop()
    max_heapify(a, 1)
    return maxv


def heap_increase_key(a, i, key):
    if key < a[i]:
        raise Exception('New key is smaller than current key.')
    a[i] = key
    while i > 1 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


def max_heap_insert(a, key):
    heap_size = len(a)
    a.append(-float('inf'))
    heap_increase_key(a, heap_size, key)
