
FILENAME = "wordsearch.txt"
SAMPLE_FILENAME = "sample_wordsearch.txt"

TARGET_WORD = "XMAS"

def get_wordsearch_grid_from_file(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            grid.append([char for char in line if char != '\n'])

    # for line in grid:
    #     print(line)
    return grid

def get_neighbour_coords(grid, i, j):
    neighbour_coords = []

    for new_i in range(i-1, i+2):
        if new_i < 0 or new_i >= len(grid):
            continue

        for new_j in range(j-1, j+2):
            if new_j < 0 or new_j >= len(grid[new_i]):
                continue

            if not (new_i == i and new_j == j):
                neighbour_coords.append((new_i, new_j))

    return neighbour_coords

def check_cell(grid, x, y, val):
    if x < 0 or x >= len(grid):
        return False

    if y < 0 or y >= len(grid[x]):
        return False

    return grid[x][y] == val

def scan_direction(grid, start_x, start_y, x_dir, y_dir):
    for i, target_char in enumerate(TARGET_WORD):
        x = start_x + x_dir * i
        y = start_y + y_dir * i

        if not check_cell(grid, x, y, target_char):
            return False
    return True

def wordsearch(filename):
    grid = get_wordsearch_grid_from_file(filename)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == TARGET_WORD[0]:
                if len(TARGET_WORD) == 1:
                    count += 1
                    continue

                neighbour_coords = get_neighbour_coords(grid, i, j)

                for coord in neighbour_coords:
                    if grid[coord[0]][coord[1]] == TARGET_WORD[1]:
                        if len(TARGET_WORD) == 2:
                            count += 1
                            continue

                        i_dir = coord[0] - i
                        j_dir = coord[1] - j
                        if scan_direction(grid, i, j, i_dir, j_dir):
                            count += 1
                            # print(i, j, i_dir, j_dir)

    return count


if __name__ == "__main__":
    print(wordsearch(FILENAME))
