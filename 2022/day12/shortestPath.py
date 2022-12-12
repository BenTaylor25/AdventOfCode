
def read_elevations(filename):
    elevations = []

    with open(filename) as file:
        for line in file.readlines():
            row = []
            for c in line.strip('\n'):
                row.append(ord(c) - ord('a'))
            elevations.append(row)
    
    return elevations

def get_start_end(elevations):
    start = None
    end = None
    for r, row in enumerate(elevations):
        for c, col in enumerate(row):
            if col == -14:   # S
                elevations[r][c] = 0
                start = (r, c)
            elif col == -28:   # E
                elevations[r][c] = 25
                end = (r, c)

    assert start != None
    assert end != None

    return start, end

def get_neighbours(x, elevations):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            # neighbour maybe
            nm = (x[0]+i, x[1]+j)
            if abs(i) + abs(j) == 1:
                if 0 <= nm[0] < len(elevations) and 0 <= nm[1] < len(elevations[0]) and elevations[nm[0]][nm[1]] <= elevations[x[0]][x[1]] + 1:
                    neighbours.append((x[0]+i, x[1]+j))
    return neighbours

def bfs_find_dist(elevations, start, end):
    q = []
    ls = []
    prev = {}

    q.insert(0, start)


    while len(q) > 0:
        s = q.pop()

        if s not in ls:
            ls.insert(0, s)

            neighbours = get_neighbours(s, elevations)

            for n in neighbours:
                if n not in ls:
                    prev[n] = s
                    q.insert(0, n)

    counter = 1
    p = prev[end]
    while p in prev:
        counter += 1
        p = prev[p]

    return counter

def main():
    elevations = read_elevations("./elevationActual.txt")
    start, end = get_start_end(elevations)

    shortest = bfs_find_dist(elevations, start, end)
    print(shortest)

if __name__ == '__main__':
    main()
