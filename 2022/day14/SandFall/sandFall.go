package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
)

func getLines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var lines []string

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func createEmptyGrid(displaySize int) [][]string {
	var grid [][]string

	for x := 0; x < displaySize*2+1; x++ {
		var row []string

		for y := 0; y < displaySize*2+1; y++ {
			row = append(row, ".")
		}

		grid = append(grid, row)
	}

	return grid
}

func main() {
	// lines := getLines("rockSample.txt")
	displaySize := 7   // how far left/right from centre

	grid := createEmptyGrid(displaySize)

	for _, row := range grid {
		for _, object := range row {
			fmt.Print(object)
		}
		fmt.Println()
	}
}
