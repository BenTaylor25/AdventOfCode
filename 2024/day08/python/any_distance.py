from antinode_counter import *

def compute_antinodes_for_pair_of_antennas(map_, location1, location2):
    delta_i = location1[0] - location2[0]
    delta_j = location1[1] - location2[1]

    antinode_locations = []

    for d in range(-len(map_), len(map_)):
        antinode_location = (location1[0] + delta_i * d, location1[1] + delta_j * d)

        antinode_locations.append(antinode_location)

    # Filter out locations that are outside of the map.
    antinode_locations = list(filter(
        lambda location : 0 <= location[0] < len(map_) and 0 <= location[1] < len(map_[location[0]]),
        antinode_locations
    ))

    return antinode_locations

# Python hack to overwrite function.
import antinode_counter
antinode_counter.compute_antinodes_for_pair_of_antennas = \
    compute_antinodes_for_pair_of_antennas

if __name__ == "__main__":
    print(antinode_counter.antinode_counter(FILENAME))
