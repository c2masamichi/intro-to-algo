package chapter02

import (
	"math"
)

func insertionSort(a []float64) {
	for j := 1; j < len(a); j++ {
		key := a[j]
		i := j - 1
		for i >= 0 && a[i] > key {
			a[i+1] = a[i]
			i--
		}
		a[i+1] = key
	}
}

func merge(a []float64, p, q, r int) {
	n1 := q - p + 1
	n2 := r - q
	left := make([]float64, n1+1)
	right := make([]float64, n2+1)
	for i := 0; i < n1; i++ {
		left[i] = a[p+i]
	}
	for j := 0; j < n2; j++ {
		right[j] = a[q+j+1]
	}
	left[n1] = math.Inf(0)
	right[n2] = math.Inf(0)
	i := 0
	j := 0
	for k := p; k <= r; k++ {
		if left[i] <= right[j] {
			a[k] = left[i]
			i++
		} else {
			a[k] = right[j]
			j++
		}
	}
}

func mergeSort(a []float64, p, r int) {
	if p < r {
		q := (p + r) / 2
		mergeSort(a, p, q)
		mergeSort(a, q+1, r)
		merge(a, p, q, r)
	}
}
