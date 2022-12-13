INT_TYPE = type(1)
LIST_TYPE = type(list())

def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file.readlines():
            lines.append(line.strip('\n'))
    return lines


def get_pairs(filename):
    all_pairs = []
    current_pair = []
    lines = get_lines(filename)
    for line in lines:
        if line == '':
            all_pairs.append(current_pair)
            current_pair = []
        else:
            current_pair.append(eval(line))
    if len(current_pair):
        all_pairs.append(current_pair)

    return all_pairs

def compare_lists(a, b):
    if type(a) == type(b) == INT_TYPE:
        if a < b:
            return 1
        if a > b:
            return -1
        return 0
    else:
        if type(a) == INT_TYPE:
            a = [a]
        if type(b) == INT_TYPE:
            b = [b]

        for cl in [compare_lists(ai, bi) for ai, bi in zip(a,b)]:
            if cl != 0:
                return cl

        if len(a) < len(b):
            return 1
        if len(a) > len(b):
            return -1
        return 0

def right_order():
    pairs = get_pairs("packetsActual.txt")
    right_pairs = []

    current_pair = 0
    for pair in pairs:
        current_pair += 1
        if compare_lists(pair[0], pair[1]) in [0, 1]:
            right_pairs.append(current_pair)
    
    print(right_pairs)
    print(sum(right_pairs))


if __name__ == '__main__':
    right_order()
