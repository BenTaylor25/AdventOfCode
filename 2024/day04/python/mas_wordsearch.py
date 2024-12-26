from wordsearch import *

TARGET = "MAS"
assert len(TARGET) == 3

def get_x_neighbour_coords(grid, i, j):
    neighbour_coords = []

    for new_i in range(i-1, i+2, 2):
        if new_i < 0 or new_i >= len(grid):
            continue

        for new_j in range(j-1, j+2, 2):
            if new_j < 0 or new_j >= len(grid[new_i]):
                continue

            if not (new_i == i and new_j == j):
                neighbour_coords.append((new_i, new_j))

    return neighbour_coords


def mas_wordsearch(filename):
    grid = get_wordsearch_grid_from_file(filename)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == TARGET[1]:
                neighbour_coords = get_x_neighbour_coords(grid, i, j)

                if len(neighbour_coords) != 4:
                    continue

                neighbour_values = [grid[i][j] for i,j in neighbour_coords]

                first_letter_count = neighbour_values.count(TARGET[0])
                last_letter_count = neighbour_values.count(TARGET[-1])

                diag_are_different = grid[i-1][j-1] != grid[i+1][j+1]

                if first_letter_count == 2 and last_letter_count == 2 and diag_are_different:
                    count += 1
                    # print(f"({i}, {j})")
    return count


if __name__ == "__main__":
    print(mas_wordsearch(FILENAME))
