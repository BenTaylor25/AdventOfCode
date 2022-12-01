
def read_calories() -> list[int]:
    calorie_counts = [0]
    with open("./calories_actual.txt", 'r') as f:
        for line in f:
            if '\n' in line:
                line = line[:-1]

            if line == '':
                calorie_counts.append(0)
            else:
                calorie_counts[-1] += int(line)

    return calorie_counts


def main():
    calorie_counts = read_calories()
    print(calorie_counts)
    print()
    print(max(calorie_counts))


if __name__ == '__main__':
    main()
