package chapter06

import (
	"reflect"
	"testing"
)

func TestParent(t *testing.T) {
	parameters := []struct {
		k        int
		expected int
	}{
		{3, 1},
		{4, 1},
	}

	for i, param := range parameters {
		k, expected := param.k, param.expected
		actual := parent(k)
		if actual != expected {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}

func TestLeft(t *testing.T) {
	parameters := []struct {
		k        int
		expected int
	}{
		{0, 1},
		{1, 3},
		{2, 5},
	}

	for i, param := range parameters {
		k, expected := param.k, param.expected
		actual := left(k)
		if actual != expected {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}

func TestRight(t *testing.T) {
	parameters := []struct {
		k        int
		expected int
	}{
		{0, 2},
		{1, 4},
		{2, 6},
	}

	for i, param := range parameters {
		k, expected := param.k, param.expected
		actual := right(k)
		if actual != expected {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}

func TestMaxHeapify(t *testing.T) {
	parameters := []struct {
		a        []float64
		k        int
		expected []float64
	}{
		{
			[]float64{3, 4, 5, 2, 1}, 0,
			[]float64{5, 4, 3, 2, 1},
		},
		{
			[]float64{16, 4, 10, 14, 7, 9, 3, 2, 8, 1}, 1,
			[]float64{16, 14, 10, 8, 7, 9, 3, 2, 4, 1},
		},
	}

	for i, param := range parameters {
		a, k, expected := param.a, param.k, param.expected
		maxHeapify(a, k, len(a)-1)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestBuildMaxHeap(t *testing.T) {
	parameters := []struct {
		a        []float64
		expected []float64
	}{
		{
			[]float64{1, 2, 3, 4, 5},
			[]float64{5, 4, 3, 1, 2},
		},
		{
			[]float64{4, 1, 3, 2, 16, 9, 10, 14, 8, 7},
			[]float64{16, 14, 10, 8, 7, 9, 3, 2, 4, 1},
		},
	}

	for i, param := range parameters {
		a, expected := param.a, param.expected
		buildMaxHeap(a)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestHeapsort(t *testing.T) {
	parameters := []struct {
		a        []float64
		expected []float64
	}{
		{
			[]float64{2, 3, 2, 1},
			[]float64{1, 2, 2, 3},
		},
		{
			[]float64{4, 1, 3, 2, 16, 9, 10, 14, 8, 7},
			[]float64{1, 2, 3, 4, 7, 8, 9, 10, 14, 16},
		},
	}

	for i, param := range parameters {
		a, expected := param.a, param.expected
		heapsort(a)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestHeapMaximum(t *testing.T) {
	a := []float64{3, 2, 1}
	var expected float64 = 3
	actual := heapMaximum(a)
	if actual != expected {
		t.Errorf("actual: %v\nexpected: %v", actual, expected)
	}
}
