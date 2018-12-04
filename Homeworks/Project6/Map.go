package main

import "fmt"

func square(a int) int {
	return a * a
}
func Map(f func(int) int, arr []int) []int {
	length := len(arr)
	for i := 0; i < length; i++ {
		arr[i] = f(arr[i])
	}
	return arr
}

func main() {
	arrayin := []int{1, 2, 3, 4, 5}
	Map(square, arrayin)
	fmt.Println(arrayin)
	arrayout := Map(func(a int) int { return a + a }, arrayin)
	fmt.Println(arrayout)
}
