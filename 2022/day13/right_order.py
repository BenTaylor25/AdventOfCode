
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

def right_order():
    pairs = get_pairs("packetsSample.txt")
    for p in pairs:
        print(p)

if __name__ == '__main__':
    right_order()
