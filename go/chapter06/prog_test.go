package chapter06

import (
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

func TestHeapMaximum(t *testing.T) {
	a := []float64{3, 2, 1}
	var expected float64 = 3
	actual := heapMaximum(a)
	if actual != expected {
		t.Errorf("actual: %v\nexpected: %v", actual, expected)
	}
}
