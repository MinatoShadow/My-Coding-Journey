package main

import "fmt"

func AreaCalculator() {
	fmt.Println("Welcome To Area Calculator Of Rectangle") // Welcome user
	// Initialising variables
	var length, breadth float64
	var unit string

	fmt.Print("Enter Length: ")
	fmt.Scan(&length) // Asking for length
	fmt.Print("Enter Breadth: ")
	fmt.Scan(&breadth) // Asking for breadth
	fmt.Print("Enter Unit: ")
	fmt.Scan(&unit) // Asking for unit

	area := length * breadth // Calculate Area

	fmt.Printf("Area of Rectangle is %v%v²\n", area, unit) // Print area
}
