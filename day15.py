filename = 'input/day15_input.txt'
moves = ""
mat = []
x, y = 0, 0
cnt = 0

with open(filename) as f:
    for line in f:
        if "#" in line:
            mat.append(list(line.strip()))
            if x > 0 and y > 0:
                continue
            for i in range(len(line)):
                if line[i] == "@":
                    x = len(mat)-1
                    y = i
        elif "<" in line:
            moves += line.strip()
# print(len(moves))

def part1(moves: str, mat: list):
    global x
    global y
    # move the robot
    for m in moves:
        if m == "<":
            if y-1 < 0 or mat[x][y-1] == "#":
                continue
            elif mat[x][y-1] == '.':
                mat[x][y] = '.'
                y -= 1
                mat[x][y] = '@'
            else:
                mat = try_push(mat, 0, -1)
                # print(mat)
        elif m == ">":
            if y+1 > len(mat[0]) or mat[x][y+1] == "#":
                continue
            elif mat[x][y+1] == '.':
                mat[x][y] = '.'
                y += 1
                mat[x][y] = '@'
            else:
                mat = try_push(mat, 0, 1)
                # print_mat(mat)
        elif m == "^":
            if x-1 < 0 or mat[x-1][y] == "#":
                continue
            elif mat[x-1][y] == '.':
                mat[x][y] = '.'
                x -= 1
                mat[x][y] = '@'
            else:
                mat = try_push(mat, -1, 0)
        elif m == "v":
            if x+1 > len(mat) or mat[x+1][y] == "#":
                continue
            elif mat[x+1][y] == '.':
                mat[x][y] = '.'
                x += 1
                mat[x][y] = '@'
            else:
                mat = try_push(mat, 1, 0)
        # print(m)
        # print_mat(mat)
    ans = 0
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] == 'O':
                ans += i*100 + j
    print(ans)

def try_push(mat:list, dx, dy):
    global x
    global y
    # find end of O's
    global cnt
    i, j = x+dx, y+dy
    while 0 <= i < len(mat) and 0 <= j < len(mat[0]):
        if mat[i][j] == 'O':
            cnt += 1
        else:
            break
        i += dx
        j += dy
    # print(i, j, dx, dy)
    if mat[i][j] == '.':
        # print('hi')
        while i != x or j != y:
            mat[i][j] = mat[i-dx][j-dy]
            i -= dx
            j -= dy
            # print_mat(mat)
        mat[x][y] = '.'
        x += dx
        y += dy
        # print_mat(mat)
    return mat

def print_mat(mat: list):
    for i in mat:
        for j in i:
            print(j, end="")
        print("")

def part2(moves:str, mat:list):
    global x
    global y
    global cnt
    mat2 = []
    for i in mat:
        cnt = 0
        mat2.append([])
        for j in i:
            if j == '#':
                mat2[-1].append('#')
                mat2[-1].append('#')
            elif j == 'O':
                mat2[-1].append('[')
                mat2[-1].append(']')
            elif j == '.':
                mat2[-1].append('.')
                mat2[-1].append('.')
            elif j == '@':
                mat2[-1].append('@')
                mat2[-1].append('.')
                x = len(mat2)-1
                y = cnt
            cnt += 2
    for m in moves:
        if m == "<":
            if y-1 < 0 or mat2[x][y-1] == "#":
                continue
            elif mat2[x][y-1] == '.':
                mat2[x][y] = '.'
                y -= 1
                mat2[x][y] = '@'
            else:
                mat2 = try_push_hor(mat2, -1)
                # print(mat)
        elif m == ">":
            if y+1 > len(mat2[0]) or mat2[x][y+1] == "#":
                continue
            elif mat2[x][y+1] == '.':
                mat2[x][y] = '.'
                y += 1
                mat2[x][y] = '@'
            else:
                mat2 = try_push_hor(mat2, 1)
        elif m == "^":
            if x-1 < 0 or mat2[x-1][y] == "#":
                continue
            elif mat2[x-1][y] == '.':
                mat2[x][y] = '.'
                x -= 1
                mat2[x][y] = '@'
            else:
                mat2 = try_push_ver(mat2, -1)
        elif m == "v":
            if x+1 > len(mat2) or mat2[x+1][y] == "#":
                continue
            elif mat2[x+1][y] == '.':
                mat2[x][y] = '.'
                x += 1
                mat2[x][y] = '@'
            else:
                mat2 = try_push_ver(mat2, 1)
        # if cnt == 8440 or cnt == 8439:
        #     print(m, cnt)
        #     print_mat(mat2)
        #     if cnt == 8440:
        #         break
        # if check_mismatch(mat2) is False:
        #     print(m, cnt)
        #     print_mat(mat2)
        #     break
        cnt += 1
    ans = 0
    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            if mat2[i][j] == '[':
                ans += i*100 + j
    print(ans)

def check_mismatch(mat: list) -> bool:
    for i in range(1, len(mat)-1):
        for j in range(2, len(mat[0])-2):
            if mat[i][j] == '[' and mat[i][j+1] != "]":
                return False
            elif mat[i][j] == ']' and mat[i][j-1] != "[":
                return False
    return True

def try_push_hor(mat, dy):
    global x
    global y
    # find end of O's
    j = y+dy
    while 0 <= j < len(mat[0]):
        if mat[x][j] != '[' and mat[x][j] != ']':
            break
        j += dy
    # print(x, j, dy)
    if mat[x][j] == '.':
        # print('hi')
        while j != y:
            mat[x][j] = mat[x][j-dy]
            j -= dy
            # print_mat(mat)
        mat[x][y] = '.'
        y += dy
        # print_mat(mat)
    return mat

def try_push_ver(mat:list, dx:int):
    global x
    global y
    global cnt
    # find end of O's
    i = x+dx
    sj, ej = y, y
    if mat[i][y] == '[':
        ej = y+1
    else:
        sj = y-1
    push = True
    rgs = [(sj, ej)]
    while 0 <= i < len(mat):
        ns, ne = sj, ej
        no_box = True
        for j in range(sj,ej+1):
            if mat[i][j] == '#':
                push = False
                break
            elif mat[i][j] == '[' or mat[i][j] == ']':
                no_box = False
        if not push or no_box:
            break
        if mat[i][sj] == ']':
            ns = sj-1
            ne = sj
        else:
            for j in range(sj, ej+1):
                if mat[i][j] == '[':
                    ns = j
                    ne = j+1
                    break
        if mat[i][ej] == '[':
            ne = ej+1
            ns = min(ns, ej)
        else:
            for j in range(ej, sj-1, -1):
                if mat[i][j] == ']':
                    ne = j
                    ns = min(ns, j-1)
                    break
        # print(ns, ne)
        i += dx
        sj, ej = ns, ne
        rgs.append((sj, ej))
    if not push:
        return mat
    # pushing logic time
    c = len(rgs)-1
    while i != x:
        # if cnt >= 8439:
        #     print(i, rgs[c][0], rgs[c][1])
        for j in range(rgs[c][0], rgs[c][1]+1):
            if mat[i-dx][j] == '#':
                continue
            elif i-dx == x and j != y:
                mat[i][j] = '.'
            else:
                mat[i][j] = mat[i-dx][j]
            if i-dx != x and (mat[i-dx][j] == '[' or mat[i-dx][j] == ']'):
                mat[i-dx][j] = '.'
        i -= dx
        c -= 1
    mat[x][y] = '.'
    x += dx
    return mat
    


part2(moves, mat)