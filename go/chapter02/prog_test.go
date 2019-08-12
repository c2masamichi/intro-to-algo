package chapter02

import (
	"reflect"
	"testing"
)

func TestInsertionSort(t *testing.T) {
	parameters := []struct {
		a        []float64
		expected []float64
	}{
		{[]float64{3}, []float64{3}},
		{[]float64{3, 4, 1, 2}, []float64{1, 2, 3, 4}},
		{[]float64{2, 5, 4, 1, 3, 2, 3}, []float64{1, 2, 2, 3, 3, 4, 5}},
	}

	for i, param := range parameters {
		a, expected := param.a, param.expected
		insertionSort(a)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestMerge(t *testing.T) {
	parameters := []struct {
		a        []float64
		p        int
		q        int
		r        int
		expected []float64
	}{
		{[]float64{3, 4, 1, 2}, 0, 1, 3, []float64{1, 2, 3, 4}},
		{[]float64{5, 8, 6, 7, 3, 4, 1, 2}, 0, 1, 3, []float64{5, 6, 7, 8, 3, 4, 1, 2}},
		{[]float64{5, 8, 6, 7, 3, 4, 1, 2}, 4, 5, 7, []float64{5, 8, 6, 7, 1, 2, 3, 4}},
	}

	for i, param := range parameters {
		a, p, q, r, expected := param.a, param.p, param.q, param.r, param.expected
		merge(a, p, q, r)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestMergeSort(t *testing.T) {
	parameters := []struct {
		a        []float64
		expected []float64
	}{
		{[]float64{3}, []float64{3}},
		{[]float64{3, 4, 1, 2}, []float64{1, 2, 3, 4}},
		{[]float64{2, 5, 4, 1, 3, 2, 3}, []float64{1, 2, 2, 3, 3, 4, 5}},
	}

	for i, param := range parameters {
		a, expected := param.a, param.expected
		mergeSort(a, 0, len(a)-1)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}
