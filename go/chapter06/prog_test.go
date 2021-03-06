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

func TestHeapExtractMax(t *testing.T) {
	parameters := []struct {
		a     []float64
		max   float64
		after []float64
	}{
		{
			[]float64{4},
			4, []float64{},
		},
		{
			[]float64{4, 2, 3, 1},
			4, []float64{3, 2, 1},
		},
		{
			[]float64{16, 14, 10, 8, 7, 9, 3, 2, 4, 1},
			16, []float64{14, 8, 10, 4, 7, 9, 3, 2, 1},
		},
	}

	for i, param := range parameters {
		a, expectedMax, after := param.a, param.max, param.after
		actualMax, a := heapExtractMax(a)
		if actualMax != expectedMax {
			t.Errorf("actual: %v\nexpected: %v", actualMax, expectedMax)
		}
		if !reflect.DeepEqual(a, after) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, after)
		}
	}
}

func TestHeapIncreaseKey(t *testing.T) {
	parameters := []struct {
		a        []float64
		index    int
		key      float64
		expected []float64
	}{
		{
			[]float64{3, 2, 1}, 1, 4,
			[]float64{4, 3, 1},
		},
		{
			[]float64{16, 14, 10, 8, 7, 9, 3, 2, 4, 1}, 8, 15,
			[]float64{16, 15, 10, 14, 7, 9, 3, 2, 8, 1},
		},
	}

	for i, param := range parameters {
		a, index, key, expected := param.a, param.index, param.key, param.expected
		heapIncreaseKey(a, index, key)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}

func TestMaxHeapInsert(t *testing.T) {
	parameters := []struct {
		a        []float64
		key      float64
		expected []float64
	}{
		{
			[]float64{4, 3, 2}, 1,
			[]float64{4, 3, 2, 1},
		},
		{
			[]float64{4, 3, 2}, 5,
			[]float64{5, 4, 2, 3},
		},
		{
			[]float64{16, 14, 10, 8, 7, 9, 3, 2, 4, 1}, 15,
			[]float64{16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7},
		},
	}

	for i, param := range parameters {
		a, key, expected := param.a, param.key, param.expected
		a = maxHeapInsert(a, key)
		if !reflect.DeepEqual(a, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, a, expected)
		}
	}
}
