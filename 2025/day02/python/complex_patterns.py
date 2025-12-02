import sum_of_invalid_ids

def is_id_invalid(id):
    id_str = str(id)

    max_pattern_size = round(len(id_str)/2)

    for pattern_size in range(1, max_pattern_size + 1):
        pattern = id_str[:pattern_size]
        pattern_repeats = len(id_str) // len(pattern)

        if id_str == pattern * pattern_repeats:
            print(id_str,pattern, pattern * pattern_repeats)
            return True

    return False

sum_of_invalid_ids.is_id_invalid = is_id_invalid

if __name__ == "__main__":
    id_ranges = sum_of_invalid_ids.get_id_ranges_from_file(
        sum_of_invalid_ids.FILENAME
    )
    print(sum_of_invalid_ids.sum_of_invalid_ids(id_ranges))
