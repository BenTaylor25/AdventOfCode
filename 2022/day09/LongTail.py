# Credit for the stepping stone
# https://topaz.github.io/paste/#XQAAAQBXCQAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLiqZwdO8DftYzG7xETHPvhjXpLhVBtGHxiJr7yn4tjI2iyRb/7n/gXbNlVB4eTFC9qDqbwwm0sASx0Z8gruN/cpWo3PsqaJQNRlzQ47B8QLNgr2bUJjl8BZcN0NVVirhGXWQi4bttrV6pezOOAK/ZdraXGryuUsNApUzbrGEJCSEUZkxzt1dCmsSXHs3aMqiBUX5GwRQ3QMMYIBPAcCDea0C9WjAUreNLk+ondYhGF8Cxb2hwJcWlLUuP1rHy1b6anwj7rb0VU+iPKaZtZm19xlZujEL3HkOJlyFWwJFJyF6AG6SuFJvoqEhVcrqYed2BPKv0ccDlD2fe7Udakb1nUvWDZ45j0Xk8e4YLpwdhjSUJU7v9BVYhPHUeJC2/8ecOywDr2/2fFpNVatPQ2e2Q7v/ZLeOTpEy2LweGSSa8RgLNFChmWag3u2lObV1DpCVUgfrj7S4rBc053CghV222Y+h/muiYlqZpArexEooJpH2QfP53rBLK9Ai3t+wplMZsAyEcRoIuxvDzqz0tqHSB4RX6xSaG2OJoZLJyRX2v66EwERXStSn3yzG0+c1MUHnDbCCIa6rHfKgY5NNtUQoQJ2eF388wPTIsJVXxGna3P2GuHEveAb46Yl6Es80I+dZ1uovGIjj3vjMRSwjmiZwDCb/QO44imXEq+ZfC9TJTIqyYpQGYAqH55VQ760zTCBTAp63sucfbv1GrHzD84WIrscDIuks+k6o76PCG4XkgXKnVsmVViRG8ubvJALgNvFInw5xAPJ9wON2nt00CIVOOe/aEOopO+SNGH4cUi1b1FS9kCbdqKPB7rbBaOqGqkHWY9TOr1GJwIocX2THOLG+6eW3VRDbYuBLYBLFKv4oYRWAfAqQvIV6uUQtD2mS7plOCjlC1QQN8hfYpX1VcC/rH05V5c5sqNhfmaSzj0xs4esFi37/E8i1joSP/4RloC

def multi_knot_visited(knots: int, motions: list[tuple[str, int]]) -> int:
    chain = [(0, 0) for _ in range(knots)]

    visited = [chain[-1]]

    for move, dist in motions:
        for i in range(dist):

            match move:
                case 'U': chain[0] = (chain[0][0], chain[0][1]+1)
                case 'D': chain[0] = (chain[0][0], chain[0][1]-1)
                case 'L': chain[0] = (chain[0][0]-1, chain[0][1])
                case 'R': chain[0] = (chain[0][0]+1, chain[0][1])

            for knot in range(1, knots):

                xdist = chain[knot][0] - chain[knot - 1][0]
                ydist = chain[knot][1] - chain[knot - 1][1]
                if xdist*xdist + ydist*ydist < 4:
                    break

                if chain[knot][1] == chain[knot - 1][1]:
                    if chain[knot][0] < chain[knot - 1][0]:
                        chain[knot] = (chain[knot][0]+1, chain[knot][1])
                    else:
                        chain[knot] = (chain[knot][0]-1, chain[knot][1])
                elif chain[knot][0] == chain[knot - 1][0]:
                    if chain[knot][1] < chain[knot - 1][1]:
                        chain[knot] = (chain[knot][0], chain[knot][1] + 1)
                    else:
                        chain[knot] = (chain[knot][0], chain[knot][1] - 1)
                else:
                    if chain[knot][0] < chain[knot - 1][0]:
                        chain[knot] = (chain[knot][0]+1, chain[knot][1])
                    else:
                        chain[knot] = (chain[knot][0]-1, chain[knot][1])

                    if chain[knot][1] < chain[knot - 1][1]:
                        chain[knot] = (chain[knot][0], chain[knot][1] + 1)
                    else:
                        chain[knot] = (chain[knot][0], chain[knot][1] - 1)

            if chain[-1] not in visited:
                visited.append(chain[-1]) 

    # print(visited)

    print(len(visited))

def run() -> None:
    with open("ropeMoveActual.txt") as f:
        motions = [(move, int(dist)) for move, dist in (line.rstrip().split(" ") for line in f)]

    multi_knot = multi_knot_visited(10, motions)

if __name__ == '__main__':
    run()
