filename = 'input/day16_input.txt'
maze = []

with open(filename) as f:
    for line in f:
        maze.append(list(line.strip()))


def part1(maze):
    m = int(1000 ** len(maze))
    score = [[[m for _ in range(4)] for _ in range(len(maze[0]))] for _ in range(len(maze))]
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    q = [(0, len(maze)-2, 1, 0)] # score, x, y, d
    score[len(maze)-2][1][0] = 0
    while len(q) > 0:
        s, x, y, d = q.pop(0)
        if x == 1 and y == len(maze[1])-2:
            continue
        dx, dy = dirs[d]
        # forward
        # print(score[x][y][d])
        alt = score[x][y][d] + 1
        if 0<=x+dx<len(maze) and 0<=y+dy<len(maze[0]) and maze[x+dx][y+dy] != '#' and alt < score[x+dx][y+dy][d]:
            score[x+dx][y+dy][d] = alt
            q.append((alt, x+dx, y+dy, d))
        # left and right
        alt = score[x][y][d] + 1001
        if dx == 0:
            if x+1 < len(maze) and maze[x+1][y] != '#' and alt < score[x+1][y][3]:
                score[x+1][y][3] = alt
                q.append((alt, x+1, y, 3))
            if 0 <= x-1 and maze[x-1][y] != '#' and alt < score[x-1][y][1]:
                score[x-1][y][1] = alt
                q.append((alt, x-1, y, 1))
        elif dy == 0:
            if y+1 < len(maze[0]) and maze[x][y+1] != '#' and alt < score[x][y+1][0]:
                score[x][y+1][0] = alt
                q.append((alt, x, y+1, 0))
            if 0 <= y-1 and maze[x][y-1] != '#' and alt < score[x][y-1][2]:
                score[x][y-1][2] = alt
                q.append((alt, x, y-1, 2))
        q.sort()
    ans = score[1][len(maze[1])-2][0]
    for i in range(1, 4):
        ans = min(ans, score[1][len(maze[1])-2][i])
    return ans

def part2(maze):
    m = int(1000 ** len(maze))
    score = [[[m for _ in range(4)] for _ in range(len(maze[0]))] for _ in range(len(maze))]
    prev = {}
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    q = [(0, len(maze)-2, 1, 0)] # score, x, y, d
    score[len(maze)-2][1][0] = 0
    while len(q) > 0:
        s, x, y, d = q.pop(0)
        if x == 1 and y == len(maze[1])-2:
            continue
        dx, dy = dirs[d]
        # print(s, x, y, d)
        if (x, y, d) not in prev:
            prev[(x, y, d)] = []
        # forward
        alt = s + 1
        if 0<=x+dx<len(maze) and 0<=y+dy<len(maze[0]) and maze[x+dx][y+dy] != '#':
            if (x+dx, y+dy, alt) not in prev:
                prev[(x+dx, y+dy, alt)] = []
            if alt < score[x+dx][y+dy][d]:
                score[x+dx][y+dy][d] = alt
                q.append((alt, x+dx, y+dy, d))
            prev[(x+dx, y+dy, alt)].append((x, y, s))
        # rotate
        alt += 1000
        if dx == 0:
            if x+1 < len(maze) and maze[x+1][y] != '#':
                # up
                if (x+1, y, alt) not in prev:
                    prev[(x+1, y, alt)] = []
                if alt < score[x+1][y][3]:
                    score[x+1][y][3] = alt
                    q.append((alt, x+1, y, 3))
                prev[(x+1, y, alt)].append((x, y, s))
            # down
            if x-1 >= 0 and maze[x-1][y] != '#':
                if (x-1, y, alt) not in prev:
                    prev[(x-1, y, alt)] = []
                if alt < score[x-1][y][1]:
                    score[x-1][y][1] = alt
                    q.append((alt, x-1, y, 1))
                prev[(x-1, y, alt)].append((x, y, s))
        elif dy == 0:
            # right
            if y+1 < len(maze[0]) and maze[x][y+1] != '#':
                if (x, y+1, alt) not in prev:
                    prev[(x, y+1, alt)] = []
                if alt < score[x][y+1][0]:
                    score[x][y+1][0] = alt
                    q.append((alt, x, y+1, 0))
                prev[(x, y+1, alt)].append((x, y, s))
            # left
            if y-1 >= 0 and maze[x][y-1] != '#':
                if (x, y-1, alt) not in prev:
                    prev[(x, y-1, alt)] = []
                if alt <= score[x][y-1][2]:
                    score[x][y-1][2] = alt
                    q.append((alt, x, y-1, 2))
                prev[(x, y-1, alt)].append((x, y, s))
        q.sort()
    ans = score[1][len(maze[1])-2][0]
    w = []
    cnt = 0
    vis = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    for i in range(1, 4):
        ans = min(ans, score[1][len(maze[1])-2][i])
    w.extend(prev[(1, len(maze[1])-2, ans)])
    while len(w) > 0:
        x, y, s = w.pop(0)
        vis[x][y] = True
        for p in prev[(x, y, s)]:
            w.append(p)
        # print(x, y, d)
    vis[1][len(maze[0])-2] = True
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if vis[i][j] is True:
                cnt += 1
                print(1, end="")
            else:
                print(" ", end="")
        print("")
    print(cnt, ans)


part2(maze)