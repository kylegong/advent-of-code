package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	nums := []int{3, 8, 9, 1, 2, 5, 4, 6, 7} // Example
	nums = []int{2, 1, 9, 3, 4, 7, 8, 6, 5}
	fmt.Println(part1(nums))
	fmt.Println(part2(nums))
}

func label(nums []int) string {
	var r int
	for i, n := range nums {
		if n == 1 {
			r = i
			break
		}
	}
	var strs []string
	for _, n := range nums[r+1:] {
		strs = append(strs, strconv.Itoa(n))
	}
	for _, n := range nums[:r] {
		strs = append(strs, strconv.Itoa(n))
	}
	return strings.Join(strs, "")

}

func part1(nums []int) string {
	in := make([]int, len(nums))
	for i, n := range nums {
		in[i] = n
	}
	t := mapTurner{}
	out := t.turns(in, 100)
	return label(out)
}

func extend(in []int, max int) []int {
	size := len(in)
	if max > size {
		size = max
	}
	ext := make([]int, size)
	for i, n := range in {
		ext[i] = n
	}
	for n := len(in) + 1; n <= max; n++ {
		ext[n-1] = n
	}
	return ext
}

func after(in []int, target, count int) []int {
	var last int
	for i, n := range in {
		last = i
		if n == target {
			break
		}
	}
	out := make([]int, count)
	for i := range out {
		out[i] = in[(last+1+i)%len(in)]
	}
	return out
}

func part2(nums []int) string {
	const numCups = 1_000_000
	const numTurns = 10_000_000
	in := extend(nums, numCups)
	t := mapTurner{}
	out := t.turns(in, numTurns)
	nexts := after(out, 1, 2)
	return fmt.Sprintf("%v", nexts[0]*nexts[1])
}

type turner interface {
	turns(in []int, numTurns int) (out []int)
}

func minMax(in []int) (min, max int) {
	min = in[0]
	max = in[0]
	for _, n := range in[1:] {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}
	return min, max
}

type arrayTurner struct{}

func (t arrayTurner) turns(in []int, numTurns int) (out []int) {
	min, max := minMax(in)
	out = make([]int, len(in))
	for i := 0; i < numTurns; i++ {
		i := i
		if i%10000 == 0 {
			//log.Printf("starting turn %v", i)
		}
		t.turn(in, out, min, max)
		in, out = out, in
	}
	for i, n := range in {
		out[i] = n
	}
	return out
}

func (t arrayTurner) turn(in, out []int, min, max int) {
	cur := in[0]
	pickup := in[1:4]
	pickupMap := make(map[int]bool)
	for _, p := range pickup {
		pickupMap[p] = true
	}
	dest := cur - 1
	if dest < min {
		dest = max
	}
	for pickupMap[dest] {
		dest--
		if dest < min {
			dest = max
		}
	}
	passedStart := 4
	passedEnd := passedStart
	for passedEnd < len(in) {
		n := in[passedEnd]
		passedEnd++
		if dest == n {
			break
		}
	}
	i := 0
	for pi := passedStart; pi < passedEnd; pi++ {
		out[i] = in[pi]
		i++
	}
	for _, p := range pickup {
		out[i] = p
		i++
	}
	for pi := passedEnd; pi < len(in); pi++ {
		out[i] = in[pi]
		i++
	}
	out[i] = cur
	i++
}

type chTurner struct {
	bufSize int
}

func (t chTurner) turns(inArr []int, numTurns int) (outArr []int) {
	min, max := minMax(inArr)
	in := make(chan int, t.bufSize)
	go func(in chan int) {
		defer close(in)
		for _, n := range inArr {
			in <- n
		}
	}(in)
	var out chan int
	for i := 0; i < numTurns; i++ {
		i := i
		if i%10000 == 0 {
			//log.Printf("starting turn %v", i)
		}
		out = make(chan int, t.bufSize)
		go func(in <-chan int, out chan<- int) {
			t.turn(in, out, min, max)
		}(in, out)
		in = out
	}
	outArr = make([]int, len(inArr))
	i := 0
	for n := range in {
		outArr[i] = n
		i++
	}
	return outArr
}

func (t chTurner) turn(in <-chan int, out chan<- int, min, max int) {
	defer close(out)
	cur := <-in
	var pickup []int
	for i := 0; i < 3; i++ {
		pickup = append(pickup, <-in)
	}
	pickupMap := make(map[int]bool)
	for _, p := range pickup {
		pickupMap[p] = true
	}
	dest := cur - 1
	if dest < min {
		dest = max
	}
	for pickupMap[dest] {
		dest--
		if dest < min {
			dest = max
		}
	}
	var passed []int
	for {
		n := <-in
		if dest != n {
			passed = append(passed, n)
			continue
		}
		break
	}
	for _, p := range passed {
		out <- p
	}
	out <- dest
	for _, p := range pickup {
		out <- p
	}
	for p := range in {
		out <- p
	}
	out <- cur
}

type inPlaceTurner struct{}

func (t inPlaceTurner) turns(in []int, numTurns int) (out []int) {
	min, max := minMax(in)
	start := 0
	for i := 0; i < numTurns; i++ {
		i := i
		if i%10000 == 0 {
			//log.Printf("starting turn %v", i)
		}
		start = t.turn(in, start, min, max)
	}
	out = make([]int, len(in))
	for i, n := range in {
		out[i] = n
	}
	return out
}

func (t inPlaceTurner) turn(in []int, start, min, max int) (nextStart int) {
	cur := in[start%len(in)]
	pickup := []int{
		in[(start+1)%len(in)],
		in[(start+2)%len(in)],
		in[(start+3)%len(in)],
	}
	pickupMap := make(map[int]bool)
	for _, p := range pickup {
		pickupMap[p] = true
	}
	dest := cur - 1
	if dest < min {
		dest = max
	}
	for pickupMap[dest] {
		dest--
		if dest < min {
			dest = max
		}
	}
	i := start + 4
	for {
		n := in[i%len(in)]
		in[(i-3)%len(in)] = n
		if dest == n {
			break
		}
		i++
	}
	for _, p := range pickup {
		in[(i-2)%len(in)] = p
		i++
	}
	return (start + 1) % len(in)
}

type mapTurner struct{}

func (t mapTurner) turns(in []int, numTurns int) (out []int) {
	min, max := minMax(in)
	after := make(map[int]int)
	for i, n := range in[:len(in)-1] {
		after[n] = in[i+1]
	}
	after[in[len(in)-1]] = in[0]
	start := in[0]
	for i := 0; i < numTurns; i++ {
		i := i
		if i%10000 == 0 {
			//log.Printf("starting turn %v", i)
		}
		t.turn(after, start, min, max)
		start = after[start]
	}
	last := 1
	out = make([]int, len(in))
	for i := range out {
		out[i] = after[last]
		last = after[last]
	}
	return out
}

func (t mapTurner) turn(after map[int]int, cur, min, max int) {
	pickup := make(map[int]int)
	last := cur
	for i := 0; i < 3; i++ {
		last = after[last]
		pickup[last] = after[last]
	}
	dest := cur - 1
	if dest < min {
		dest = max
	}
	for pickup[dest] != 0 {
		dest--
		if dest < min {
			dest = max
		}
	}
	afterCur := after[last]
	after[last] = after[dest]
	after[dest] = after[cur]
	after[cur] = afterCur
}
