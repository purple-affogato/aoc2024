filename = 'input/day6_input.txt'
start = (0, 0)
m = []

with open(filename) as f:
    for line in f:
        m.append(list(line.strip()))
        for i in range(len(m[-1])):
            if ord(m[-1][i]) == 94:
                start = (len(m)-1, i)

def part1():
    global m
    global start
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x = start[0]
    y = start[1]
    d = 0
    mark = "X"
    # m[x][y] = mark
    while x >= 0 and x < len(m) and y >= 0 and y < len(m[0]):
        m[x][y] = mark
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]
        # print(x, y)
        if nx < 0 or nx >= len(m) or ny < 0 or ny >= len(m[nx]):
            break
        elif m[nx][ny] == "#":
            d = (d+1)%4
            continue
        x = nx
        y = ny
    cnt = 0
    for i in m:
        for j in i:
            if j == mark:
                cnt += 1
    print(cnt)

def test_loop():
    global m
    global start
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vis = [[[0,0,0,0] for _ in range(len(m[0]))] for _ in range(len(m))]
    x, y = start
    d = 0
    while 0 <= x < len(m) and 0 <= y < len(m[0]):
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]
        if nx < 0 or nx >= len(m) or ny < 0 or ny >= len(m[0]):
            break
        elif m[nx][ny] == "#":
            # print(x, y, nx, ny, d, vis[x][y])
            if vis[x][y][d] == 1:
                return 1
            vis[x][y][d] = 1
            d = (d+1)%4
            continue
        x, y = nx, ny
    return 0

def part2():
    global m
    cnt = 0
    for i in range(len(m)):
        print(i)
        for j in range(len(m[i])):
            # print(i, j)
            if m[i][j] == ".":
                m[i][j] = "#"
                cnt += test_loop()
                m[i][j] = "."
    print(cnt)

part2()
