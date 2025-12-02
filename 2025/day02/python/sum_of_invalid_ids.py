USE_SAMPLE_FILE = False
FILENAME = "sample_" * USE_SAMPLE_FILE + "id_ranges.txt"

def get_id_ranges_from_file(filename):
    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]

    assert len(lines) == 1

    line = lines[0]

    range_strs = line.split(',')

    ranges = []
    for range_str in range_strs:
        start, end = range_str.split('-')

        ranges.append((int(start), int(end)))

    return ranges

def is_id_invalid(id):
    id_str = str(id)

    is_odd_length = len(id_str) % 2 != 0
    if is_odd_length:
        return False

    mid_point = len(id_str) // 2
    first_half = id_str[:mid_point]
    last_half = id_str[mid_point:]

    return first_half == last_half

def get_invalid_ids(id_range):
    invalid_ids = []
    for id in range(id_range[0], id_range[1]+1):
        if is_id_invalid(id):
            invalid_ids.append(id)

    return invalid_ids


def sum_of_invalid_ids(id_ranges):
    invalid_ids = []

    for id_range in id_ranges:
        invalid_ids.extend(get_invalid_ids(id_range))

    print(invalid_ids)
    return sum(invalid_ids)

if __name__ == "__main__":
    id_ranges = get_id_ranges_from_file(FILENAME)
    print(sum_of_invalid_ids(id_ranges))
