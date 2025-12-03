from part1 import *

if __name__ == "__main__":
    battery_banks = get_battery_banks_from_file(False)
    print(output_joltage(battery_banks, 12))
