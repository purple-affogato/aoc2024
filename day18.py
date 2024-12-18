n = 71

def read_input():
    filename = 'input/day18_input.txt'
    b = []
    with open(filename) as f:
        for line in f:
            x,y = map(int, line.strip().split(","))
            b.append((x,y))
    return b

def part1():
    pos = read_input()
    space = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1024):
        space[pos[i][0]][pos[i][1]] = 1
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(0,0)]
    vis = [[False for _ in range(len(space))] for _ in range(len(space))]
    dis = [[0 for _ in range(len(space))] for _ in range(len(space))]
    vis[0][0] = True
    while len(q) > 0:
        x,y = q.pop(0)
        if x == n-1 and y == n-1:
            break
        for d in dirs:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<n and 0<=ny<len(space) and not vis[nx][ny] and space[nx][ny] != 1:
                vis[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))
    print(dis[n-1][n-1])

def bfs(space):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(0,0)]
    vis = [[False for _ in range(n)] for _ in range(n)]
    dis = [[0 for _ in range(n)] for _ in range(n)]
    vis[0][0] = True
    while len(q) > 0:
        x,y = q.pop(0)
        if x == n-1 and y == n-1:
            return True
        for d in dirs:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<n and 0<=ny<len(space) and not vis[nx][ny] and space[nx][ny] != 1:
                vis[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))
    return False

def part2():
    pos = read_input()
    space = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1024):
        space[pos[i][0]][pos[i][1]] = 1
    for i in range(1024, len(pos)):
        p = pos[i]
        space[p[0]][p[1]] = 1
        if bfs(space) is False:
            return i+1
    return -1

print(part2())
