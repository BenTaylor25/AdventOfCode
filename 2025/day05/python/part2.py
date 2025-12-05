from part1 import *

'''
Approach:
Convert to continuous ranges,
and sum(range.end-range.start+1)
'''

'''
Method:
continuous_ranges = []

while ranges remain
{
    cont_start = min(min(r) for r in ranges)
    cont_end = cont_start

    {
        foreach range r
            if cond_end >= r.start &
            cond_end < r.end

                cond_end = r.end
    }
    repeat until iteration with no change to cond_end

    continuous_ranges.add(cont_start, cont_end)
    remove all considered ranges
}
'''

def get_continuous_ranges(ranges):
    continuous_ranges = []

    while len(ranges) != 0:
        start_of_ranges = [r.start for r in ranges]
        cont_start = min(start_of_ranges)
        cont_end = cont_start

        changed_this_iteration = True
        while changed_this_iteration:
            changed_this_iteration = False

            for r in ranges:
                if cont_end >= r.start and cont_end < r.stop-1:
                    cont_end = r.stop-1
                    changed_this_iteration = True

        continuous_ranges.append(range(cont_start, cont_end + 1))

        # Keep ranges that haven't been considered yet
        ranges = list(filter(lambda r : r.start > cont_end, ranges))

    return continuous_ranges


def get_range_size(range_):
    return range_.stop - range_.start

def count_fresh_ingredient_ids(fresh_ranges):
    continuous_ranges = get_continuous_ranges(fresh_ranges)

    continuous_ranges_sizes = [get_range_size(r) for r in continuous_ranges]

    return sum(continuous_ranges_sizes)

if __name__ == "__main__":
    fresh_ranges, _ = get_info_from_file(False)
    print("-"*3)
    print(count_fresh_ingredient_ids(fresh_ranges))
