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

def sort_packets(pairs):
    packets = []
    for pair in pairs:
        packets.append(pair[0])
        packets.append(pair[1])
    packets.append([[2]])
    packets.append([[6]])

    for a in range(len(packets)):
        for b in range(a+1, len(packets)):
            if compare_lists(packets[a], packets[b]) == -1:
                packets[a], packets[b] = packets[b], packets[a]

    return packets

def fix_packets():
    pairs = get_pairs("packetsSample.txt")
    sorted_packets = sort_packets(pairs)

    div_1 = sorted_packets.index([[2]]) + 1
    div_2 = sorted_packets.index([[6]]) + 1

    print(div_1 * div_2)

if __name__ == '__main__':
    fix_packets()
