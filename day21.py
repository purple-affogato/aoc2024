filename = 'input/day21_input.txt'
num_pos = {}
num_pos['1'] = (2, 0)
num_pos['2'] = (2, 1)
num_pos['3'] = (2, 2)
num_pos['4'] = (1, 0)
num_pos['5'] = (1, 1)
num_pos['6'] = (1, 2)
num_pos['7'] = (0, 0)
num_pos['8'] = (0, 1)
num_pos['9'] = (0, 2)
num_pos['A'] = (3, 2)
num_pos['0'] = (3, 1)
dir_pos = {}
dir_pos['<'] = (1, 0)
dir_pos['^'] = (0, 1)
dir_pos['v'] = (1, 1)
dir_pos['>'] = (1, 2)
dir_pos['A'] = (0, 2)

def read_input():
    codes = []
    with open(filename) as f:
        for line in f:
            codes.append(line.strip())
    return codes

def solve():
    codes = read_input()
    ans = 0
    for c in codes:
        cnt = 0
        print(c)
        for i in range(len(c)):
            cur = c[i]
            prev = "A"
            if i > 0:
                prev = c[i-1]
            cnt += get_num_dist(cur, prev)
        print(cnt, int(c[:-1]))
        ans += cnt * int(c[:-1])
        # print(ans)
    print(ans)
        
            

def get_num_dist(cur: str, prev:str):
    p1 = num_pos[prev]
    p2 = num_pos[cur]
    hor = p2[1] - p1[1]
    ver = p2[0] - p1[0]
    hor_str = ""
    ver_str = ""
    if hor < 0:
        hor_str += "<" * abs(hor)
    elif hor > 0:
        hor_str += ">" * abs(hor)
    if ver < 0:
        ver_str += "^" * abs(ver)
    elif ver > 0:
        ver_str += "v" * abs(ver)
    process1 = ver_str+hor_str+"A"
    process2 = hor_str+ver_str+"A"
    # print(prev, cur, process1, process2)
    # part 1
    # if (cur == '0' or cur == 'A') and (prev == '1' or prev == '4' or prev == '7'):
    #     return len(get_pad_dist(get_pad_dist(process2)))
    # elif (cur == '7' or cur == '4' or cur == '1') and (prev == '0' or prev == 'A'):
    #     return len(get_pad_dist(get_pad_dist(process1)))
    # r1 = get_pad_dist(get_pad_dist(process1))
    # r2 = get_pad_dist(get_pad_dist(process2))

    # part 2
    ctr = 25
    if (cur == '0' or cur == 'A') and (prev == '1' or prev == '4' or prev == '7'):
        # only calculate for process2
        r2 = part2(process2, ctr)
        # print(r2)
        return r2
    elif (cur == '7' or cur == '4' or cur == '1') and (prev == '0' or prev == 'A'):
        r1 = part2(process1, ctr)
        # print(r1)
        return r1
    r1 = part2(process1, ctr)
    r2 = part2(process2, ctr)
    # print(r1, r2)
    return min(r1,r2)

dp = {} # state = (prev, cur)
# at each state: dict(iteration number: result)

def part2(p: str, ctr:int) -> int:
    global dp
    if ctr == 0:
        return len(p)
    result = 0
    for i in range(len(p)):
        prev = 'A'
        if i > 0:
            prev = p[i-1]
        if prev == p[i]:
            result += 1
            continue
        
        if (prev, p[i]) not in dp:
            dp[(prev, p[i])] = {}
        if ctr not in dp[(prev, p[i])]:
            if prev == '<':
                dp[(prev, p[i])][ctr] = part2(dir_pad_dist_hor(prev, p[i]), ctr-1)
            elif p[i] == '<':
                dp[(prev, p[i])][ctr] = part2(dir_pad_dist_ver(prev, p[i]), ctr-1)
            else:
                dp[(prev, p[i])][ctr] = min(part2(dir_pad_dist_hor(prev, p[i]), ctr-1), part2(dir_pad_dist_ver(prev, p[i]), ctr-1))
        # print(prev, p[i], ctr, dp[(prev, p[i])][ctr])
        result += dp[(prev, p[i])][ctr]
        # print(result)
    return result
        

def dir_pad_dist_ver(prev:str, cur:str):
    p1 = dir_pos[prev]
    p2 = dir_pos[cur]
    hor = p2[1] - p1[1]
    ver = p2[0] - p1[0]
    hor_str = ""
    ver_str = ""
    if hor < 0:
        hor_str += "<" * abs(hor)
    elif hor > 0:
        hor_str += ">" * abs(hor)
    if ver < 0:
        ver_str += "^" * abs(ver)
    elif ver > 0:
        ver_str += "v" * abs(ver)
    return ver_str + hor_str + "A"

def dir_pad_dist_hor(prev:str, cur:str):
    p1 = dir_pos[prev]
    p2 = dir_pos[cur]
    hor = p2[1] - p1[1]
    ver = p2[0] - p1[0]
    hor_str = ""
    ver_str = ""
    if hor < 0:
        hor_str += "<" * abs(hor)
    elif hor > 0:
        hor_str += ">" * abs(hor)
    if ver < 0:
        ver_str += "^" * abs(ver)
    elif ver > 0:
        ver_str += "v" * abs(ver)
    return hor_str + ver_str + "A"

def directional_robot(p: str):
    result = ""
    for i in range(len(p)):
        prev = 'A'
        if i > 0:
            prev = p[i-1]
            if p[i] == p[i-1]:
                result += 'A'
                continue
        process = dir_pad_dist_ver(prev, p[i])
        result += process
    return result

solve()