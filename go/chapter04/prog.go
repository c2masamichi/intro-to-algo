package chapter04

import (
	"math"
)

func findMaxCrossingSubarray(a []float64, low, mid, high int) (int, int, float64) {
	leftSum := math.Inf(-1)
	sum := float64(0)
	maxLeft := mid
	for i := mid; i >= low; i-- {
		sum += a[i]
		if sum > leftSum {
			leftSum = sum
			maxLeft = i
		}
	}

	rightSum := math.Inf(-1)
	sum = float64(0)
	maxRight := mid + 1
	for j := mid + 1; j <= high; j++ {
		sum += a[j]
		if sum > rightSum {
			rightSum = sum
			maxRight = j
		}
	}

	return maxLeft, maxRight, leftSum + rightSum
}

func findMaximumSubarray(a []float64, low, high int) (int, int, float64) {
	if high == low {
		return low, high, a[low]
	}
	mid := (low + high) / 2
	leftLow, leftHigh, leftSum := findMaximumSubarray(a, low, mid)
	rightLow, rightHigh, rightSum := findMaximumSubarray(a, mid+1, high)
	crossLow, crossHigh, crossSum := findMaxCrossingSubarray(a, low, mid, high)

	if leftSum >= rightSum && leftSum >= crossSum {
		return leftLow, leftHigh, leftSum
	} else if rightSum >= leftSum && rightSum >= crossSum {
		return rightLow, rightHigh, rightSum
	} else {
		return crossLow, crossHigh, crossSum
	}
}

func squareMatrixMultiply(a, b [][]float64) [][]float64 {
	n := len(a)
	c := make([][]float64, n)
	for i := 0; i < n; i++ {
		c[i] = make([]float64, n)
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				c[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return c
}
