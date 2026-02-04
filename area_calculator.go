package main

import "fmt"

func main() {
	fmt.Println("Welcome To Area Calculator Of Rectangle")

	var length float64
	fmt.Print("Enter Length: ")
	fmt.Scan(&length)

	var breadth float64
	fmt.Print("Enter Breadth: ")
	fmt.Scan(&breadth)

	var unit string
	fmt.Print("Enter Unit: ")
	fmt.Scan(&unit)

	var area float64 = length * breadth
	fmt.Printf("Area of Rectange is %v%v²", area, unit)
}
