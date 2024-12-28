import itertools

FILENAME = "antenna_locations.txt"
SAMPLE_FILENAME = "sample_antenna_locations.txt"

EMPTY_SPACE_CHAR = '.'

def get_map_from_file(filename):
    map_ = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')

            map_.append([char for char in line])

    return map_

def get_antenna_chars_from_map(map_):
    antenna_chars = []

    for row in map_:
        for char in row:
            char_is_antenna = char != EMPTY_SPACE_CHAR
            antenna_is_new = char not in antenna_chars

            char_is_new_antenna = char_is_antenna and antenna_is_new

            if char_is_new_antenna:
                antenna_chars.append(char)
    
    return antenna_chars

def find_all_locations_of_antenna_frequency(map_, antenna_char):
    locations = []

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == antenna_char:
                locations.append((i, j))
    
    return locations

def compute_antinodes_for_pair_of_antennas(map_, location1, location2):
    delta_i = location1[0] - location2[0]
    delta_j = location1[1] - location2[1]

    antinode_locations = [
        (location1[0] + delta_i, location1[1] + delta_j),
        (location2[0] - delta_i, location2[1] - delta_j)
    ]

    # Filter out locations that are outside of the map.
    antinode_locations = list(filter(
        lambda location : 0 <= location[0] < len(map_) and 0 <= location[1] < len(map_[location[0]]),
        antinode_locations
    ))

    return antinode_locations

def compute_antinodes(map_, antenna_chars):
    antinode_locations = []

    for antenna_char in antenna_chars:
        antenna_locations_of_char = \
            find_all_locations_of_antenna_frequency(map_, antenna_char)

        for pair in itertools.combinations(antenna_locations_of_char, r=2):
            a, b = pair

            antinode_locations.extend(compute_antinodes_for_pair_of_antennas(map_, a, b))

    return antinode_locations

def antinode_counter(filename):
    map_ = get_map_from_file(filename)

    antenna_chars = get_antenna_chars_from_map(map_)
    antinode_locations = compute_antinodes(map_, antenna_chars)
    unique_antinode_locations = set(antinode_locations)

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == EMPTY_SPACE_CHAR and (i,j) in antinode_locations:
                print('#', end='')
            else:
                print(map_[i][j], end='')
        print()
    print()

    # print(antinode_locations)
    return len(unique_antinode_locations)

if __name__ == "__main__":
    print(antinode_counter(FILENAME))
