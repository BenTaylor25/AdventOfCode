from trailhead_score_counter import *

def trailhead_ratings(filename):
    map_ = load_map_from_file(filename)

    trailheads = find_all_trailheads(map_)

    trailhead_peak_lists = [traverse_trail_upwards(map_, trailhead) for trailhead in trailheads]

    trailhead_ratings = [len(x) for x in trailhead_peak_lists]

    return sum(trailhead_ratings)

if __name__ == "__main__":
    print(trailhead_ratings(FILENAME))
