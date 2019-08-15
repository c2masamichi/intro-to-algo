package chapter04

import (
	"reflect"
	"testing"
)

func TestFindMaxCrossingSubarray(t *testing.T) {
	type result struct {
		left  int
		right int
		sum   float64
	}
	parameters := []struct {
		a        []float64
		low      int
		mid      int
		high     int
		expected result
	}{
		{
			[]float64{1, 2, 3, 4, 5}, 0, 2, 4,
			result{0, 4, 15},
		},
		{
			[]float64{10, -1, -1, -1, -1, -1, -1, 10}, 1, 3, 6,
			result{3, 4, -2},
		},
		{
			[]float64{-2, 3, -2, 3, 4, 2, -5, -1}, 0, 3, 7,
			result{1, 5, 10},
		},
	}

	for i, param := range parameters {
		a, low, mid, high, expected := param.a, param.low, param.mid, param.high, param.expected
		left, right, sum := findMaxCrossingSubarray(a, low, mid, high)
		actual := result{left, right, sum}
		if actual != expected {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}

func TestFindMaximumSubarray(t *testing.T) {
	type result struct {
		left  int
		right int
		sum   float64
	}
	parameters := []struct {
		a        []float64
		low      int
		high     int
		expected result
	}{
		{
			[]float64{5}, 0, 0,
			result{0, 0, 5},
		},
		{
			[]float64{10, 11, 21}, 1, 1,
			result{1, 1, 11},
		},
		{
			[]float64{2, 2, 2, 2, 2}, 0, 4,
			result{0, 4, 10},
		},
		{
			[]float64{-2, -3, -1, -2, -5}, 0, 4,
			result{2, 2, -1},
		},
		{
			[]float64{-2, -2, -2, -2, -2}, 0, 4,
			result{0, 0, -2},
		},
		{
			[]float64{10, -5, -6, 5, 6, -2, -3, 2}, 0, 7,
			result{3, 4, 11},
		},
	}

	for i, param := range parameters {
		a, low, high, expected := param.a, param.low, param.high, param.expected
		left, right, sum := findMaximumSubarray(a, low, high)
		actual := result{left, right, sum}
		if actual != expected {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}

func TestSquareMatrixMultiply(t *testing.T) {
	parameters := []struct {
		a        [][]float64
		b        [][]float64
		expected [][]float64
	}{
		{
			[][]float64{{1, 2}, {3, 4}},
			[][]float64{{1, 0}, {0, 1}},
			[][]float64{{1, 2}, {3, 4}},
		},
		{
			[][]float64{{1, 2}, {3, 4}},
			[][]float64{{2, 1}, {1, 2}},
			[][]float64{{4, 5}, {10, 11}},
		},
	}

	for i, param := range parameters {
		a, b, expected := param.a, param.b, param.expected
		actual := squareMatrixMultiply(a, b)
		if !reflect.DeepEqual(actual, expected) {
			t.Errorf("i: %d\nactual: %v\nexpected: %v", i, actual, expected)
		}
	}
}
