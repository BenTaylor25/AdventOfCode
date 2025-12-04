from part1 import *

def remove_rolls_iteration(rolls):
    removable_rolls = []

    for i in range(len(rolls)):
        for j in range(len(rolls[i])):
            if rolls[i][j] == '@':
                if count_neighbour_paper(rolls, i, j) < 4:
                    removable_rolls.append((i, j))
    
    return removable_rolls

def remove_rolls(rolls):
    rolls_removed = 0

    while True:
        removable_rolls = remove_rolls_iteration(rolls)

        if removable_rolls == []:
            return rolls_removed

        for (i, j) in removable_rolls:
            rolls[i][j] = '.'
            rolls_removed += 1

if __name__ == "__main__":
    rolls = get_rolls_of_paper_from_file(False)
    rolls = [list(row) for row in rolls]
    print(remove_rolls(rolls))
