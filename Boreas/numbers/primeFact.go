package main

import (
	"fmt"
)

func decompose(n int) []int {
	factors := []int{}
	for n%2 == 0 {
		factors = append(factors, 2)
		n = n / 2
	}
	for i := 3; i*i <= n; i += 2 {
		for n%i == 0 {
			factors = append(factors, i)
			n = n / i
		}
	}
	if n > 2 {
		factors = append(factors, n)
	}
	return factors
}

func main() {
	var num int
	fmt.Print("Enter a number: ")
	fmt.Scan(&num)
	dec := decompose(num)
	fmt.Println("Prime factors: ", dec)
}
