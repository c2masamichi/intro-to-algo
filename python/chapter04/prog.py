def find_max_crossing_subarray(a, low, mid, high):
    left_sum = -float('inf')
    sumv = 0
    for i in range(mid, low - 1, -1):
        sumv += a[i]
        if sumv > left_sum:
            left_sum = sumv
            max_left = i

    right_sum = -float('inf')
    sumv = 0
    for j in range(mid + 1, high + 1):
        sumv += a[j]
        if sumv > right_sum:
            right_sum = sumv
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(a, low, high):
    if high == low:
        return low, high, a[low]
    else:
        mid = (low+high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(
            a, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(
            a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(
            a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def square_matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c
