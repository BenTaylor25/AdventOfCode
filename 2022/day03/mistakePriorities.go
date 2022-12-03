package main;

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"sort"
)

func getLines(filename string) []string {
	file, err := os.Open(filename);
	if err != nil {
		log.Fatal(err);
	}
	defer file.Close();

	var lines []string;

	scanner := bufio.NewScanner(file);
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func getSplitLines(filename string) [][]string {
	lines := getLines(filename)

	var split [][]string

	for _, ln := range lines {
		lineLen := len(ln)
		splitln := []string{ln[0:lineLen/2], ln[lineLen/2:lineLen]}

		split = append(split, splitln)
	}

	return split
}

func sortString(str string) string {
	strRune := []rune(str)

	sort.Slice(strRune, func(i, j int) bool {
		return strRune[i] < strRune[j]
	})

	return string(strRune)
}

func findSameInBoth(ln []string) string {
	// compOne := []rune(ln[0])
	// sort.Slice(compOne, func(i, j int) bool {
	// 	return compOne[i] < compOne[j]
	// })
	// compOneS := string(compOne)
	compOneS := sortString(ln[0])
	fmt.Println(compOneS)

	// compTwo := []rune(ln[1])
	// sort.Slice(compTwo, func(i, j int) bool {
	// 	return compTwo[i] < compTwo[j]
	// })
	// compTwoS := string(compTwo)
	compTwoS := sortString(ln[1])
	fmt.Println(compTwoS)

	fmt.Println()

	return "-"
}

func main() {
	splitLines := getSplitLines("rucksackSample.txt")
	// fmt.Println(splitLines)

	for _, ln := range splitLines {
		sameInBoth := findSameInBoth(ln)
		fmt.Println(sameInBoth)
	}
	
}

