from greater_than_previous import *

def collect_triple_sweep_sums(lst):
    triple_sweep_sums = [
        sum(lst[i-2:i+1])
        for i in range(2, len(lst))
    ]

    return triple_sweep_sums

def triple_sweep(filename):
    sonar_values = get_sonar_values(filename)

    triple_sweep_values = collect_triple_sweep_sums(sonar_values)

    deltas = [
        triple_sweep_values[i] - triple_sweep_values[i-1]
        for i in range(1, len(triple_sweep_values))
    ]

    positive_deltas = list(filter(lambda x : x > 0, deltas))

    print(len(positive_deltas))

if __name__ == "__main__":
    triple_sweep(FILENAME)
