filename = 'input/day10_input.txt'
hiking = []
ans = 0

with open(filename) as f:
    for line in f:
        hiking.append(list(map(int, list(line.strip()))))

def score(h: list, x:int, y:int) -> int:
    result = 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    vis = [[False for _ in range(len(h[0]))] for _ in range(len(h))]
    q = [(x, y)]
    while len(q) > 0:
        cur = q.pop(0)
        x = cur[0]
        y = cur[1]
        if h[x][y] == 9:
            result += 1
            continue
        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < len(h) and 0 <= ny < len(h[0]) and h[nx][ny] == h[x][y]+1 and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx, ny))
    return result

def part1(h: list):
    ans = 0
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] == 0:
                ans += score(h, i, j)
    print(ans)

def rating(h, i, j, cnt):
    if h[i][j] == 9:
        cnt [i][j] += 1
        return
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for d in dirs:
        nx = i + d[0]
        ny = j + d[1]
        if 0 <= nx < len(h) and 0 <= ny < len(h[0]) and h[nx][ny] == h[i][j]+1:
            rating(h, nx, ny, cnt)

def part2(h: list):
    ans = 0
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j] == 0:
                cnt = [[0 for _ in range(len(h[0]))] for _ in range(len(h))]
                rating(h, i, j, cnt)
                for a in range(len(h)):
                    for b in range(len(h[0])):
                        if h[a][b] == 9:
                            ans += cnt[a][b]
                
    print(ans)

part2(hiking)