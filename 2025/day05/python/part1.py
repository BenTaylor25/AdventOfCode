
FILENAME = "inventory.txt"

def get_info_from_file(use_sample):
    filename = "sample_" * use_sample + FILENAME

    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]

    split_idx = lines.index("")

    fresh_ranges_strs = lines[:split_idx]
    available_ids_strs = lines[split_idx+1:]

    fresh_ranges = []
    for fresh_ranges_str in fresh_ranges_strs:
        start_str, end_str = fresh_ranges_str.split('-')

        start_incl = int(start_str)
        end_incl = int(end_str) + 1

        fresh_ranges.append(range(start_incl, end_incl))

    available_ids = [int(id_str) for id_str in available_ids_strs]

    print(fresh_ranges)
    print(available_ids)

    return fresh_ranges, available_ids

def is_in_fresh(fresh_ranges, available_id):
    for fresh_range in fresh_ranges:
        if available_id in fresh_range:
            return True

    return False

def count_available_in_fresh(fresh_ranges, available_ids):
    number_in_fresh = 0

    for available_id in available_ids:
        if is_in_fresh(fresh_ranges, available_id):
            number_in_fresh += 1

    return number_in_fresh

if __name__ == "__main__":
    fresh_ranges, available_ids = get_info_from_file(False)
    print(count_available_in_fresh(fresh_ranges, available_ids))
