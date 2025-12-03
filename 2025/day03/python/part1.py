from typing import List

FILENAME = "battery_banks.txt"

def get_battery_banks_from_file(use_sample) -> List[str]:
    filename = "sample_" * use_sample + FILENAME

    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]

    return lines

def idx_of_largest_digit(nums: List[int]):
    assert len(nums) > 0

    largest_idx = 0
    largest_num = nums[0]

    for idx, num in enumerate(nums):
        if num > largest_num:
            largest_idx = idx
            largest_num = num

    return largest_idx, largest_num

def highest_joltage(bank, max_enabled_batteries):
    bank_ints = [int(battery) for battery in bank]

    joltage = ""

    # An a-digit number is always greater than a b-digit number if a > b.
    # The highest joltage in the bank will ALMOST always start with the
    # largest digit.
    # The exception is when it causes us to have a number of n-digits where
    # n < max_enabled_batteries; e.g. [1,2,9]; the largest joltage with
    # max_enabled_batteries=2 is 29.
    # The pattern here is that we ignore the last max_enabled_batteries-1
    # digits when selecting the next best digit.
    joltage_len = min(len(bank), max_enabled_batteries)
    previous_idx = -1

    for i in range(joltage_len):
        bank_ints_range = bank_ints[previous_idx+1:len(bank)-joltage_len+1+i]
        idx, num = idx_of_largest_digit(bank_ints_range)

        joltage += str(num)
        previous_idx = previous_idx+1 + idx
    
    return int(joltage)

def output_joltage(battery_banks, max_enabled_batteries):
    highest_joltage_per_bank = \
        [highest_joltage(bank, max_enabled_batteries) for bank in battery_banks]

    print(highest_joltage_per_bank)

    return sum(highest_joltage_per_bank)

if __name__ == "__main__":
    battery_banks = get_battery_banks_from_file(False)
    print(output_joltage(battery_banks, 2))
