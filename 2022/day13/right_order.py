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
    assert type(a) == LIST_TYPE
    assert type(b) == LIST_TYPE
    zab = list(zip(a, b))

    i = -1
    comp_value = 0
    while comp_value == 0 and i < min(len(a), len(b))-1:
        i += 1
        ai, bi = zab[i]

        if type(ai) == type(bi) == LIST_TYPE:
            comp_value = compare_lists(ai, bi)
        elif type(ai) == LIST_TYPE:
            comp_value = compare_lists(ai, [bi])
        elif type(bi) == LIST_TYPE:
            comp_value = compare_lists([ai], bi)
        else:
            # both int
            if ai < bi:
                comp_value = 1
            elif ai > bi:
                comp_value = -1

    if comp_value == 0:
        if i == len(a) - 1:
            comp_value = 1
        else:
            comp_value = -1

    return comp_value


def right_order():
    pairs = get_pairs("packetsActual.txt")
    right_pairs = []

    current_pair = 0
    for pair in pairs:
        current_pair += 1
        if compare_lists(pair[0], pair[1]) == 1:
            right_pairs.append(current_pair)
    
    print(sum(right_pairs))


if __name__ == '__main__':
    right_order()
