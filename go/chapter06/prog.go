package chapter06

func parent(i int) int {
	return (i - 1) / 2
}

func left(i int) int {
	return 2*i + 1
}

func right(i int) int {
	return 2 * (i + 1)
}

func maxHeapify(a []float64, i, heapSize int) {
	leftIndex := left(i)
	rightIndex := right(i)
	largest := i
	if leftIndex <= heapSize && a[leftIndex] > a[i] {
		largest = leftIndex
	}
	if rightIndex <= heapSize && a[rightIndex] > a[largest] {
		largest = rightIndex
	}
	if largest != i {
		a[i], a[largest] = a[largest], a[i]
		maxHeapify(a, largest, heapSize)
	}
}

func buildMaxHeap(a []float64) {
	length := len(a) - 1
	for i := (length - 1) / 2; i >= 0; i-- {
		maxHeapify(a, i, length)
	}
}

func heapMaximum(a []float64) float64 {
	return a[0]
}
