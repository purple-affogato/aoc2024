filename = 'input/day9_input.txt'
nums = []

with open(filename) as f:
    for line in f:
        tmp = list(line)
        for t in tmp:
            nums.append(int(t))

def make_disk(n:list):
    disk = []
    pos = []
    d = -1
    empty = 0
    for i in range(len(n)):
        # print(n[i])
        add = d
        if i % 2 == 0:
            d += 1
            add = d
        else:
            add = -1
            empty += n[i]
        for i in range(n[i]):
            disk.append(add)
            if add >= 0:
                pos.append(len(disk)-1)
    # print(disk)
    return disk, pos, empty
                

def part1(n: list):
    disk, pos, empty = make_disk(n)
    # print(disk, pos)
    for i in range(len(disk)):
        if empty == 0:
            break
        if disk[i] < 0:
            if pos[-1] > i:
                p = pos.pop()
                disk[i] = disk[p]
                disk[p] = -1
            # print(disk[i], p)
            # empty -= 1
        # print(disk[i], empty)
    ans = 0
    # print(disk)
    for i in range(len(disk)):
        if disk[i] < 0:
            continue
        ans += i * disk[i]
        # print(i, disk[i], ans)
    print(ans)

def part2(n: list):
    blocksize = []
    disk = []
    b_pos = []
    for i in range(len(n)):
        if i % 2 == 0:
            blocksize.append(n[i])
            b_pos.append(len(disk))
            for j in range(n[i]):
                disk.append(len(blocksize)-1)
        else:
            # empty.append(n[i])
            for j in range(n[i]):
                disk.append(-1)
    print(b_pos)
    for i in range(len(blocksize)-1, 0, -1):
        empty = 0
        start = 0
        for j in range(len(disk)):
            if j >= b_pos[i]:
                break
            if disk[j] < 0:
                empty += 1
                if empty == 1:
                    start = j
            else:
                empty = 0
            if empty >= blocksize[i]:
                for k in range(blocksize[i]):
                    disk[start+k] = i
                    disk[b_pos[i] + k] = -1
                break
        print(i)
    ans = 0
    for i in range(len(disk)):
        if disk[i] < 0:
            continue
        ans += i * disk[i]
        # print(i, disk[i], ans)
    print(ans)

part2(nums)