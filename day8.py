filename = 'input/day8_input.txt'
roof = []

with open(filename) as f:
    for line in f:
        roof.append(list(line.strip()))

def get_pts(r: list):
    freq_pts = {}
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] != '.':
                if r[i][j] not in freq_pts:
                    freq_pts[r[i][j]] = []
                freq_pts[r[i][j]].append((i, j))
    return freq_pts

def part1(r: list):
    freq_pts = get_pts(r)
    cnt = 0
    for k in freq_pts:
        # print(k)
        for i in range(len(freq_pts[k])):
            for j in range(i+1, len(freq_pts[k])):
                p1 = freq_pts[k][i]
                p2 = freq_pts[k][j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                n1 = (p1[0] + dx, p1[1] + dy)
                n2 = (p2[0] - dx, p2[1] - dy)
                if 0 <= n1[0] < len(r) and 0 <= n1[1] < len(r[0]) and r[n1[0]][n1[1]] != '#':
                    r[n1[0]][n1[1]] = '#'
                    cnt += 1
                if 0 <= n2[0] < len(r) and 0 <= n2[1] < len(r[0]) and r[n2[0]][n2[1]] != '#':
                    r[n2[0]][n2[1]] = '#'
                    cnt += 1
                # print(n1, n2, cnt)
    print(cnt)
    # for i in r:
    #     for j in i:
    #         print(j, end="")
    #     print("\n", end="")

def part2(r: list):
    freq_pts = get_pts(r)
    cnt = 0
    for k in freq_pts:
        # print(k)
        for i in range(len(freq_pts[k])):
            p1 = freq_pts[k][i]
            r[p1[0]][p1[1]] = "#"
            for j in range(i+1, len(freq_pts[k])):
                p2 = freq_pts[k][j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                n1 = [p1[0] + dx, p1[1] + dy]
                n2 = [p2[0] - dx, p2[1] - dy]
                while 0 <= n1[0] < len(r) and 0 <= n1[1] < len(r[0]):
                    r[n1[0]][n1[1]] = '#'
                    # cnt += 1
                    n1[0] += dx
                    n1[1] += dy
                while 0 <= n2[0] < len(r) and 0 <= n2[1] < len(r[0]):
                    r[n2[0]][n2[1]] = '#'
                    # cnt += 1
                    n2[0] -= dx
                    n2[1] -= dy
                # print(n1, n2, cnt)
    for i in r:
        for j in i:
            # print(j, end="")
            if j == "#":
                cnt += 1
        # print("\n", end="")
    print(cnt)

part2(roof)
