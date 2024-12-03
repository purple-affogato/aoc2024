import re

enable = True
filename = 'day3_input.txt'
ans = 0

def part1(muls):
    ctr = 0
    for (x, y) in muls:
        ctr += int(x) * int(y)
    return ctr

def part2(muls):
    global enable
    ctr = 0
    for (a, b, c, d, e) in muls:
        if e == "don't()":
            enable = False
        elif d == "do()":
            enable = True
        elif enable:
            ctr += int(b) * int(c)
    return ctr

with open(filename) as f:
    for line in f:
        # muls1 = re.findall(r'mul\((\d+),(\d+)\)', line) # part 1
        muls = re.findall(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', line) # part 2
        # print(len(muls), len(muls1))
        ans += part2(muls)
print(ans)
