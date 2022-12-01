
from most_calories import read_calories

TOPN = 3

def main():
    calorie_counts = read_calories()

    assert len(calorie_counts) >= TOPN

    topn_calories = []
    for _ in range(TOPN):
        top = max(calorie_counts)
        calorie_counts.remove(top)   # remove first occurence
        topn_calories.append(top)

    print(sum(topn_calories))


if __name__ == '__main__':
    main()

