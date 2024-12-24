
FILENAME = "location_ids.txt"
SAMPLE_FILENAME = "sample_location_ids.txt"

def get_lists_from_file(filename):
    list1 = []
    list2 = []

    with open(filename) as f:
        for line in f.readlines():
            line_spl = line.strip('\n').split()
            assert len(line_spl) == 2, line_spl

            list1.append(line_spl[0])
            list2.append(line_spl[1])

    return list1, list2

def get_lists_delta(list1, list2):
    delta = [abs(int(x) - int(y)) for x, y in zip(list1, list2)]
    return delta

def location_id_distances():
    list1, list2 = get_lists_from_file(FILENAME)
    list1.sort()
    list2.sort()
    lists_delta = get_lists_delta(list1, list2)
    total_distance = sum(lists_delta)
    return total_distance

if __name__ == "__main__":
    total_distance = location_id_distances()
    print(total_distance)
