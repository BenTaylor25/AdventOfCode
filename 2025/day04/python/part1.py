from typing import List

FILENAME = "rolls_of_paper.txt"

def get_rolls_of_paper_from_file(use_sample) -> List[str]:
    filename = "sample_" * use_sample + FILENAME

    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]

    return lines

def count_neighbour_paper(rolls, y, x):
    neighbours = 0

    for i in range(max(0, y-1), min(len(rolls), y+2)):
        for j in range(max(0, x-1), min(len(rolls[i]), x+2)):
            if not (i == y and j == x):
                if rolls[i][j] == '@':
                    neighbours += 1

    return neighbours

def find_accessible_rolls(rolls):
    accessible_rolls = 0

    for i in range(len(rolls)):
        for j in range(len(rolls[i])):
            if rolls[i][j] == '@':
                if count_neighbour_paper(rolls, i, j) < 4:
                    accessible_rolls += 1

    return accessible_rolls

if __name__ == "__main__":
    rolls = get_rolls_of_paper_from_file(False)
    print(find_accessible_rolls(rolls))
