package chapter02

import (
	"reflect"
	"testing"
)

func TestInsertionSort(t *testing.T) {
	a := []int{3, 4, 1, 2}
	insertionSort(a)
	expected := []int{1, 2, 3, 4}
	if !reflect.DeepEqual(a, expected) {
		t.Errorf("actual: %v\nexpected: %v", a, expected)
	}
}
