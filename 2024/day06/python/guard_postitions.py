
SAMPLE_FILENAME = "sample_guard_map.txt"
FILENAME = "guard_map.txt"

GUARD_CHAR = '^'
OBSTRUCTION_CHAR = '#'
GUARD_VISITED_CHAR = 'X'

UP_DIR = [-1, 0]
DOWN_DIR = [1, 0]
LEFT_DIR = [0, -1]
RIGHT_DIR = [0, 1]

DIRECTIONS = [UP_DIR, RIGHT_DIR, DOWN_DIR, LEFT_DIR]

def get_map_from_file(filename):
    map_ = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')

            map_.append([tile for tile in line])

    return map_

def get_guard_starting_point(map_):
    for i, row in enumerate(map_):
        if GUARD_CHAR in row:
            j = row.index(GUARD_CHAR)
            return (i, j)

    raise Exception("Guard not found.")

def guard_traversal(map_, guard_location, guard_direction):
    guard_on_map = True

    while guard_on_map:
        # Update map tile.
        map_[guard_location[0]][guard_location[1]] = GUARD_VISITED_CHAR

        # Calculate forward location.
        forward_location = [location + direction for location, direction in zip(guard_location, guard_direction)]
        forward_location_on_map = \
            0 <= forward_location[0] < len(map_) and \
            0 <= forward_location[1] < len(map_[0])

        # Check if guard is on the map.
        if not forward_location_on_map:
            guard_on_map = False
            break

        # Should turn if there is an obstruction in the forward location.
        should_turn = map_[forward_location[0]][forward_location[1]] == OBSTRUCTION_CHAR

        if should_turn:
            # Turn.
            idx = DIRECTIONS.index(guard_direction)
            new_idx = (idx + 1) % len(DIRECTIONS)
            new_direction = DIRECTIONS[new_idx]
            guard_direction = new_direction

        else:
            # Step.
            guard_location = forward_location

def count_distinct_locations(map_):
    count = 0

    for row in map_:
        count += row.count(GUARD_VISITED_CHAR)

    return count

def guard_positions(filename):
    map_ = get_map_from_file(filename)

    guard_location = get_guard_starting_point(map_)
    guard_direction = UP_DIR
    guard_traversal(map_, guard_location, guard_direction)

    distinct_locations = count_distinct_locations(map_)

    return distinct_locations

if __name__ == "__main__":
    print(guard_positions(FILENAME))
