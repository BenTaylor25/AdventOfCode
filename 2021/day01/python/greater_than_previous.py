
SAMEPLE_FILENAME = "sample_sonar_sweep.txt"
FILENAME = "sonar_sweep.txt"

def get_sonar_values(filename):
    with open(filename) as f:
        sonar_values = [int(x.strip('\n')) for x in f.readlines()]

    return sonar_values

def greater_than_previous(filename):
    sonar_values = get_sonar_values(filename)

    deltas = [
        sonar_values[i] - sonar_values[i-1]
        for i in range(1, len(sonar_values))
    ]

    positive_deltas = list(filter(lambda x : x > 0, deltas))

    print(len(positive_deltas))


if __name__ == "__main__":
    greater_than_previous(FILENAME)
