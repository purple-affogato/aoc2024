filename = "input/day12_input.txt"
plots = []

with open(filename) as f:
    for line in f:
        plots.append(list(line.strip()))

vis = [[False for _ in range(len(plots))] for _ in range(len(plots[0]))]

def calc_seg(prev, lo, hi):
    if lo == 0:
        return prev[hi]
    return prev[hi] - prev[lo-1]

def get_sides(pts, p):
    # print(pts)
    result = 0
    y = set()
    x = {}
    for i in range(len(pts)):
        if pts[i][1] not in x:
            x[pts[i][1]] = []
        x[pts[i][1]].append(pts[i][0])
        y.add(pts[i][1])
    y = sorted(y)
    prev: list = [0 for _ in range(len(p))]
    starts = []
    ends = []
    for i in y:
        x[i].sort()
        c = []
        cur = [0 for _ in range(len(p))]
        l = 0
        r = 0
        for seg in range(0, len(x[i])-1):
            if x[i][seg+1] - x[i][seg] > 1:
                c.append((x[i][l], x[i][r]))
                l = seg+1
                r = l
            else:
                r += 1
        c.append((x[i][l], x[i][r]))
        for seg in c:
            cur[seg[0]] = 1
            if seg[1] < len(cur)-1:
                cur[seg[1]+1] = -1
            if seg[0] not in starts:
                result += 1
            if seg[1] not in ends:
                result += 1
            gaps = 0
            last_gap = -2
            for j in range(seg[0], seg[1]+1):
                if prev[j] == 0:
                    if last_gap != j-1:
                        gaps += 1
                    last_gap = j
            result += gaps
            print(i, seg[0], seg[1], result)
        # check outer parts
        for i in range(1, len(cur)):
            cur[i] += cur[i-1]
        segs = 0
        last_seg = -2
        for j in range(0, len(prev)):
            if prev[j] == 1 and cur[j] == 0:
                print(j)
                if last_seg != j-1:
                    segs += 1
                last_seg = j
        result += segs
        print(result)
        # update stuff
        for i in range(0, len(cur)):
            prev[i] = cur[i]
        starts.clear()
        ends.clear()
        for seg in c:
            starts.append(seg[0])
            ends.append(seg[1])
    return result+len(starts)

def get_price(p:list, x, y):
    global vis
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = [(x, y)]
    area = 1
    pts = [(x, y)]
    vis[x][y] = True
    while len(q) > 0:
        i, j = q.pop(0)
        for d in dirs:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < len(p) and 0 <= nj < len(p[i]) and p[ni][nj] == p[i][j] and vis[ni][nj] is False:
                area += 1
                pts.append((ni, nj))
                q.append((ni, nj))
                vis[ni][nj] = True
    # peri = get_peri(p, pts)
    sides = get_sides(pts, p)
    print(p[x][y], area, sides, end="\n\n")
    # return area * peri
    return area * sides # part 2
    
def get_peri(p:list, pts: list):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = 0
    for x, y in pts:
        result += 4
        for d in dirs:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < len(p) and 0 <= ny < len(p[0]) and p[nx][ny] == p[x][y]:
                result -= 1
    return result

def solve(p: list):
    global vis
    ans = 0
    for i in range(len(p)):
        for j in range(len(p[i])):
            if not vis[i][j]:
                ans += get_price(p, i, j)
                # print(ans, p[i][j], i, j)
    print(ans)

solve(plots)