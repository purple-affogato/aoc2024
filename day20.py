filename = 'input/day20_input.txt'

def read_input():
    start, end = (0,0), (0,0)
    rt = []
    with open(filename) as f:
        for line in f:
            rt.append(list(line.strip()))
            for i in range(len(rt[-1])):
                if rt[-1][i] == 'S':
                    start = (len(rt)-1, i)
                elif rt[-1][i] == 'E':
                    end = (len(rt)-1, i)
    return start, end, rt

    
def part1():
    start, end, rt = read_input()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(start[0],start[1])]
    vis = [[False for _ in range(len(rt))] for _ in range(len(rt[0]))]
    dis = [[0 for _ in range(len(rt))] for _ in range(len(rt[0]))]
    pts = [(start[0],start[1])]
    vis[start[0]][start[1]] = True
    while len(q) > 0:
        x,y = q.pop(0)
        if x == end[0] and y == end[1]:
            break
        for d in dirs:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<len(rt) and 0<=ny<len(rt[0]) and not vis[nx][ny] and rt[nx][ny] != '#':
                vis[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
                pts.append((nx,ny))
                q.append((nx, ny))
    ans = dis[end[0]][end[1]]
    cnt = 0
    print(ans)
    
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            x,y = pts[i], pts[j]
            if x[0] == y[0] and abs(x[1]-y[1]) == 2 and rt[x[0]][(x[1]+y[1])//2] == '#':
                saved = dis[y[0]][y[1]] - dis[x[0]][x[1]] - 2
                if saved >= 100:
                    cnt += 1
                # print(saved, x, y, dis[x[0]][x[1]], dis[y[0]][y[1]])
            elif x[1] == y[1] and abs(x[0]-y[0]) == 2 and rt[(x[0]+y[0])//2][x[1]] == '#':
                saved = dis[y[0]][y[1]] - dis[x[0]][x[1]] - 2
                if saved >= 100:
                    cnt += 1
    print(cnt)

def part2():
    start, end, rt = read_input()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = [(start[0],start[1])]
    vis = [[False for _ in range(len(rt))] for _ in range(len(rt[0]))]
    dis = [[0 for _ in range(len(rt))] for _ in range(len(rt[0]))]
    pts = [(start[0],start[1])]
    vis[start[0]][start[1]] = True
    while len(q) > 0:
        x,y = q.pop(0)
        if x == end[0] and y == end[1]:
            break
        for d in dirs:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<len(rt) and 0<=ny<len(rt[0]) and not vis[nx][ny] and rt[nx][ny] != '#':
                vis[nx][ny] = True
                dis[nx][ny] = dis[x][y] + 1
                pts.append((nx,ny))
                q.append((nx, ny))
    ans = dis[end[0]][end[1]]
    cnt = 0
    print(ans)
    debug = {}
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            x,y = pts[i], pts[j]
            man_dist = abs((x[0]-y[0])) + abs(x[1]-y[1])
            if man_dist <= 20 and dis[y[0]][y[1]] - dis[x[0]][x[1]] > man_dist:
                saved = dis[y[0]][y[1]] - dis[x[0]][x[1]] - man_dist
                if saved >= 100:
                    # print(x, y, dis[y[0]][y[1]] - dis[x[0]][x[1]], saved, man_dist)
                    # print(abs((x[0]-y[0])), abs(x[1]-y[1]))
                    cnt += 1
                    # if saved not in debug:
                    #     debug[saved] = 0
                    # debug[saved] += 1
    print(cnt)
    # print(debug)

part2()