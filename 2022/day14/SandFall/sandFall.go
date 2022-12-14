package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"strings"
	"strconv"
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

func populateGrid(grid [][]string, lines []string, displaySize int) [][]string {
	leftX := 500 - displaySize

	grid[0][displaySize] = "+"

	for _, line := range lines {
		linesplit := strings.Split(line, " -> ")
		
		for i := 0; i < len(linesplit)-1; i++ {
			coord1s := strings.Split(linesplit[i], ",")
			coord2s := strings.Split(linesplit[i+1], ",")

			fromX, _ := strconv.Atoi(coord1s[0])
			toX, _ := strconv.Atoi(coord2s[0])
			if fromX > toX {
				fromX, toX = toX, fromX
			}
			fromY, _ := strconv.Atoi(coord1s[1])
			toY, _ := strconv.Atoi(coord2s[1])
			if fromY > toY {
				fromY, toY = toY, fromY
			}
			
			for c := fromX; c <= toX; c++ {
				for r := fromY; r <= toY; r++ {
					grid[r][c-leftX] = "#"
				}
			}

		}
		fmt.Println()
	}

	return grid
}

func isAbyssSand(grid [][]string, sandCol int) bool {
	for c := 0; c < len(grid[0]); c++ {
		colHasSand := c == sandCol
		colHasBlock := false
		for r := 0; r < len(grid); r++ {
			if grid[r][c] == "o" {
				colHasSand = true
			} else if grid[r][c] == "#" {
				colHasBlock = true
			}
		}
		if (colHasSand && !colHasBlock) {
			return true
		}
	}
	return false
}

func main() {
	lines := getLines("rockSample.txt")
	displaySize := 7   // how far left/right from centre
	leftX := 500 - displaySize

	grid := createEmptyGrid(displaySize)
	grid = populateGrid(grid, lines, displaySize)

	counter := 0
	_isAbyssSand := false
	for !_isAbyssSand {
		sandActive := true
		sandX := 500
		sandY := 0
		for sandActive {
			if grid[sandY+1][sandX-leftX] == "." {
				sandY++
			} else if grid[sandY+1][sandX-leftX-1] == "." {
				sandY++
				sandX--
			} else if grid[sandY+1][sandX-leftX+1] == "." {
				sandY++
				sandX++
			} else {
				sandActive = false
			}

			if (isAbyssSand(grid, sandX-leftX)) {
				_isAbyssSand = true
				sandActive = false
				counter--
			}
		}
		grid[sandY][sandX-leftX] = "o"
		counter++
	}

	fmt.Println()
	for _, row := range grid {
		for _, object := range row {
			fmt.Print(object)
		}
		fmt.Println()
	}

	fmt.Println(counter)
}
