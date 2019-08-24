package chapter06

import (
	"math"
)

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

func heapsort(a []float64) {
	buildMaxHeap(a)
	length := len(a) - 1
	heapSize := length
	for i := length; i >= 1; i-- {
		a[0], a[i] = a[i], a[0]
		heapSize--
		maxHeapify(a, 0, heapSize)
	}
}

func heapMaximum(a []float64) float64 {
	return a[0]
}

func heapExtractMax(a []float64) (float64, []float64) {
	heapSize := len(a) - 1
	max := a[0]
	a[0] = a[heapSize]
	a = a[:len(a)-1]
	heapSize--
	maxHeapify(a, 0, heapSize)
	return max, a
}

func heapIncreaseKey(a []float64, i int, key float64) {
	a[i] = key
	for i > 0 && a[parent(i)] < a[i] {
		a[i], a[parent(i)] = a[parent(i)], a[i]
		i = parent(i)
	}
}

func maxHeapInsert(a []float64, key float64) []float64 {
	heapSize := len(a)
	a = append(a, math.Inf(-1))
	heapIncreaseKey(a, heapSize, key)
	return a
}
