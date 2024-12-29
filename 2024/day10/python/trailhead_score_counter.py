
FILENAME = "topographic_map.txt"
SAMPLE_FILENAME = "sample_topographic_map.txt"

TRAILHEAD_TILE = 0
MAX_LEVEL = 9

def load_map_from_file(filename):
    map_ = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')
            map_.append([int(tile) for tile in line])

    return map_

def find_all_trailheads(map_):
    trailheads = []

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == TRAILHEAD_TILE:
                trailheads.append((i, j))

    return trailheads

def get_neighbours_on_map(map_, current_location):
    loc_i, loc_j = current_location

    neighbours_on_map = []

    if loc_i - 1 >= 0:
        neighbours_on_map.append((loc_i - 1, loc_j))
    if loc_i + 1 < len(map_):
        neighbours_on_map.append((loc_i + 1, loc_j))
    if loc_j - 1 >= 0:
        neighbours_on_map.append((loc_i, loc_j - 1))
    if loc_j + 1 < len(map_[loc_i]):
        neighbours_on_map.append((loc_i, loc_j + 1))
    
    return neighbours_on_map

def traverse_trail_upwards(map_, current_location):
    loc_i, loc_j = current_location
    current_level = map_[loc_i][loc_j]

    if current_level == MAX_LEVEL:
        return [current_location]

    neighbours = get_neighbours_on_map(map_, current_location)

    peaks_reached = []
    for neighbour in neighbours:
        neighbour_i, neighbour_j = neighbour
        neighbour_level = map_[neighbour_i][neighbour_j]

        if neighbour_level == current_level + 1:
            peaks_reached.extend(traverse_trail_upwards(map_, neighbour))

    return peaks_reached

def trailhead_score_counter(filename):
    map_ = load_map_from_file(filename)

    trailheads = find_all_trailheads(map_)

    trailhead_peak_lists = [traverse_trail_upwards(map_, trailhead) for trailhead in trailheads]

    # Find number of unique for each.
    trailhead_scores = [len(list(set(x))) for x in trailhead_peak_lists]

    return sum(trailhead_scores)

if __name__ == "__main__":
    print(trailhead_score_counter(FILENAME))
