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
	compOne := sortString(ln[0])
	compTwo := sortString(ln[1])

	i, j := 0, 0

	for (i < len(compOne) && j < len(compTwo) && compOne[i] != compTwo[j]) {
		if (compOne[i] < compTwo[j]) {
			i++
		} else {
			j++
		}
	}

	if (compOne[i] == compTwo[j]) {
		return string(compOne[i])
	}

	panic("no char in both")
}

func getPriority(char string) int {
	cRune := []rune(char)[0]
	cAscii := int(cRune)

	if cAscii >= 97 && cAscii <= 122 {
		// 1 - 26
		return cAscii - 96
	} else if cAscii >= 65 && cAscii <= 90 {
		// 27 - 52
		return cAscii - 38
	}

	panic("char not in alphabet")
}

func main() {
	splitLines := getSplitLines("rucksackSample.txt")
	prioritySum := 0

	for _, ln := range splitLines {
		sameInBoth := findSameInBoth(ln)
		priority := getPriority(sameInBoth)
		// fmt.Println(priority)

		prioritySum += priority
	}

	fmt.Println(prioritySum)
}

