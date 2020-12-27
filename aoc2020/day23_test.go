package main

import (
	"fmt"
	"math/rand"
	"reflect"
	"testing"
)

func TestTurns(t *testing.T) {
	for _, turner := range []turner{
		arrayTurner{},
		chTurner{},
		inPlaceTurner{},
		mapTurner{},
	} {
		t.Run(fmt.Sprintf("%T", turner), func(t *testing.T) {
			nums := []int{3, 8, 9, 1, 2, 5, 4, 6, 7}
			got := label(turner.turns(nums, 10))
			want := "92658374"
			if got != want {
				t.Errorf("Turns(10) = %v, want %v", got, want)
			}
			nums = []int{3, 8, 9, 1, 2, 5, 4, 6, 7}
			got = label(turner.turns(nums, 100))
			want = "67384529"
			if got != want {
				t.Errorf("Turns(100) = %v, want %v", got, want)
			}
		})
	}
}

func TestManyTurns(t *testing.T) {
	for _, turner := range []turner{
		arrayTurner{},
		chTurner{},
		inPlaceTurner{},
		mapTurner{},
	} {
		t.Run(fmt.Sprintf("%T", turner), func(t *testing.T) {
			nums := []int{3, 8, 9, 1, 2, 5, 4, 6, 7}
			got := fmt.Sprintf("%v", after(turner.turns(nums, 1_000_000), 1, 2))
			want := "[5 9]"
			if got != want {
				t.Errorf("Turns(1_000_000) = %v, want %v", got, want)
			}
		})
	}
}
func TestTurnsLarge(t *testing.T) {
	for _, turner := range []turner{
		arrayTurner{},
		chTurner{},
		inPlaceTurner{},
		mapTurner{},
	} {
		t.Run(fmt.Sprintf("%T", turner), func(t *testing.T) {
			nums := []int{3, 8, 9, 1, 2, 5, 4, 6, 7}
			nums = extend(nums, 100_000)
			got := fmt.Sprintf("%v", after(turner.turns(nums, 100), 1, 2))
			want := "[3 4]"
			if got != want {
				t.Errorf("Turns(1_000_000) = %v, want %v", got, want)
			}
		})
	}
}

func TestExtend(t *testing.T) {
	for i, tc := range []struct {
		in   []int
		max  int
		want []int
	}{
		{
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
			0,
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
		},
		{
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
			9,
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
		},
		{
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
			10,
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7, 10},
		},
		{
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
			15,
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7, 10, 11, 12, 13, 14, 15},
		},
		{
			[]int{},
			10,
			[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
		},
	} {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			got := extend(tc.in, tc.max)
			if !reflect.DeepEqual(got, tc.want) {
				t.Errorf("extend = %v\nwant %v", got, tc.want)
			}
		})
	}
}

func TestAfter(t *testing.T) {
	for i, tc := range []struct {
		in            []int
		target, count int
		want          []int
	}{
		{
			[]int{3, 8, 9, 1, 2, 5, 4, 6, 7},
			1, 2,
			[]int{2, 5},
		},
		{
			[]int{3, 8, 9, 2, 5, 4, 6, 1, 7},
			6, 3,
			[]int{1, 7, 3},
		},
		{
			[]int{3, 8, 9, 2, 5, 4, 6, 7, 1},
			1, 3,
			[]int{3, 8, 9},
		},
	} {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			got := after(tc.in, tc.target, tc.count)
			if !reflect.DeepEqual(got, tc.want) {
				t.Errorf("after = %v\nwant %v", got, tc.want)
			}
		})
	}
}

func BenchmarkTurns(b *testing.B) {
	for _, cfg := range []struct {
		max, turns int
	}{
		{9, 100},
		{100, 100},
		{1_000_000, 100},
		{9, 1_000_000},
		{1_000_000, 100_000},
	} {
		b.Run(fmt.Sprintf("%vx%v", cfg.max, cfg.turns), func(b *testing.B) {
			for _, turner := range []turner{
				arrayTurner{},
				// chTurner{},
				// chTurner{100},
				// inPlaceTurner{},
				mapTurner{},
			} {
				b.Run(fmt.Sprintf("%T", turner), func(b *testing.B) {
					for i := 0; i < b.N; i++ {
						nums := extend([]int{3, 8, 9, 1, 2, 5, 4, 6, 7}, cfg.max)
						rand.Shuffle(len(nums), func(i, j int) {
							nums[i], nums[j] = nums[j], nums[i]
						})
						b.StartTimer()
						turner.turns(nums, cfg.turns)
					}
				})
			}
		})
	}
}
