filename = "input/day25_input.txt"

def read_input():
    locks, keys, cur = [],[],[]
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                if cur[0][0] == '#':
                    locks.append(get_heights(cur))
                else:
                    keys.append(get_heights(cur))
                cur.clear()
            else:
                cur.append(line)

    if len(cur) > 0:
        if cur[0][0] == '#':
            locks.append(get_heights(cur))
        else:
            keys.append(get_heights(cur))
        cur.clear()
    return locks, keys

def get_heights(cur:list)->list:
    heights = []
    for i in range(5):
        ctr = 0
        for j in range(1,6):
            if cur[j][i] == '#':
                ctr += 1
        heights.append(ctr)
    return heights

def part1():
    locks, keys = read_input()
    cnt = 0
    for l in locks:
        for k in keys:
            take = True
            for i in range(5):
                if k[i] + l[i] > 5:
                    take = False
                    break
            if take is True:
                cnt += 1
    print(cnt)

part1()