package chapter05

import (
	"math"
	"math/rand"
	"sort"
	"time"
)

type pair struct {
	value    float64
	priority int
}

func sortByPriority(a []float64, p []int) {
	n := len(a)
	pairs := make([]pair, n)
	for i := 0; i < n; i++ {
		pairs[i] = pair{a[i], p[i]}
	}
	sort.SliceStable(pairs, func(i, j int) bool {
		return pairs[i].priority < pairs[j].priority
	})
	for i := 0; i < n; i++ {
		a[i] = pairs[i].value
	}
}

func permuteBySorting(a []float64) {
	n := len(a)
	p := make([]int, n)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < n; i++ {
		p[i] = rand.Intn(int(math.Pow(float64(n), 3)))
	}
	sortByPriority(a, p)
}
