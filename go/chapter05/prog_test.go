package chapter05

import (
	"reflect"
	"sort"
	"testing"
)

func TestSortByPriority(t *testing.T) {
	parameters := []struct {
		a        []float64
		p        []int
		expected []float64
	}{
		{[]float64{10}, []int{1}, []float64{10}},
		{[]float64{10, 20, 30}, []int{2, 3, 1}, []float64{30, 10, 20}},
	}

	for i, param := range parameters {
		a, p, expected := param.a, param.p, param.expected
		sortByPriority(a, p)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestPermuteBySorting(t *testing.T) {
	parameters := []struct {
		a        []float64
		expected []float64
	}{
		{[]float64{3}, []float64{3}},
		{[]float64{3, 2, 5, 1}, []float64{3, 2, 5, 1}},
		{[]float64{10, 2, 2, 4, 4, 3, 7}, []float64{10, 2, 2, 4, 4, 3, 7}},
	}

	for i, param := range parameters {
		a, expected := param.a, param.expected
		permuteBySorting(a)
		sort.Float64s(a)
		sort.Float64s(expected)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}
