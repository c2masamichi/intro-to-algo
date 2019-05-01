package chapter02

import (
	"reflect"
	"testing"
)

func TestInsertionSort(t *testing.T) {
	parameters := []struct {
		a        []int
		expected []int
	}{
		{[]int{3}, []int{3}},
		{[]int{3, 4, 1, 2}, []int{1, 2, 3, 4}},
		{[]int{2, 5, 4, 1, 3, 2, 3}, []int{1, 2, 2, 3, 3, 4, 5}},
	}

	for i, p := range parameters {
		insertionSort(p.a)
		if !reflect.DeepEqual(p.a, p.expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, p.a, p.expected)
		}
	}
}
