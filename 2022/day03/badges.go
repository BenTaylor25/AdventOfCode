package main

import "fmt"

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

	for (i < len(elfOne) && k < len(elfThr) && elfOne[i] != elfThr[k]) {
		for (i < len(compOne) && j < len(compTwo) && compOne[i] != compTwo[j]) {
			if (compOne[i] < compTwo[j]) {
				i++
			} else {
				j++
			}
		}

		if (elfOne[i] < elfThr[k]) {
			i++
		} else {
			k++
		}
	}

	if elfOne[i] == elfTwo[j] == elfThr[k] {
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

	if len(lines) % 3 {
		panic("cannot split elves into groups of 3")
	}

	prioritySum := 0
	var group []string

	for _, ln := range lines {
		group = append(group, ln)

		if len(group) == 3 {
			commonInGroup := getCommonInGroup(group)
			prioritySum += priority
			group = group[:0]
		}
	}

	fmt.Println(prioritySum)

}

