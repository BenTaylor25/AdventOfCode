from location_id_distances import get_lists_from_file

FILENAME = "location_ids.txt"
SAMPLE_FILENAME = "sample_location_ids.txt"

def convert_all_to_int(lst):
    return [int(x) for x in lst]

def similarity():
    list1, list2 = get_lists_from_file(FILENAME)
    list1 = convert_all_to_int(list1)
    list2 = convert_all_to_int(list2)

    similarity_score = 0

    for item1 in list1:
        count_in_second = list2.count(item1)

        similarity_score += item1 * count_in_second
    
    return similarity_score

if __name__ == "__main__":
    print(similarity())
