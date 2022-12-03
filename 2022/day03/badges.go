package main

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

func sortString(str string) string {
	strRune := []rune(str)

	sort.Slice(strRune, func(i, j int) bool {
		return strRune[i] < strRune[j]
	})

	return string(strRune)
}

func getCommonInGroup(grp []string) string {
	elfOne := sortString(grp[0])
	elfTwo := sortString(grp[1])
	elfThr := sortString(grp[2])

	i, j, k := 0, 0, 0

	for (i < len(elfOne) && j < len(elfTwo) && k < len(elfThr) && elfOne[i] != elfTwo[j] && elfOne[i] != elfThr[k]) {
		if (elfOne[i] < elfTwo[j]) {
			i++
		} else if (elfOne[i] > elfTwo[j]) {
			j++
		}

		if (elfOne[i] < elfThr[k]) {
			i++
		} else if (elfOne[i] > elfThr[k]) {
			k++
		}
	}

	if elfOne[i] == elfTwo[j] && elfOne[i] == elfThr[k] {
		return string(elfOne[i])
	}

	panic("no char in all")
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
	lines := getLines("rucksackSample.txt")

	if len(lines) % 3 != 0 {
		panic("cannot split elves into groups of 3")
	}

	prioritySum := 0
	var group []string

	for _, ln := range lines {
		group = append(group, ln)

		if len(group) == 3 {
			fmt.Println(group)
			commonInGroup := getCommonInGroup(group)
			prioritySum += getPriority(commonInGroup)
			group = group[:0]
		}
	}

	fmt.Println(prioritySum)

}

