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

func main() {
	lines := getLines("rockSample.txt")

	for _, line := range lines {
		fmt.Println(line)
	}
}
