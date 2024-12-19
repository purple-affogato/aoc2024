filename = 'input/day19_input.txt'

def read_input():
    towels = []
    patterns = []
    idx = 0
    with open(filename) as f:
        for line in f:
            if idx == 0:
                towels.extend(line.strip().split(", "))
            elif line.strip() != '':
                patterns.append(line.strip())
            idx += 1
    return towels, patterns

def part1():
    towels, patterns = read_input()
    cnt = 0
    for p in patterns:
        if match(p, towels) is True:
            cnt += 1
    print(cnt)

def match(p: str, towels:list):
    dp = [False for _ in range(len(p)+1)]
    dp[0] = True
    for i in range(0, len(p)+1):
        for j in range(i):
            if dp[j] is True and p[j:i] in towels:
                dp[i] = True
                break
    return dp[len(p)]

def part2():
    towels, patterns = read_input()
    cnt = 0
    for p in patterns:
        cnt += count_matches(p, towels)
    print(cnt)

def count_matches(p:str, towels:list) -> int:
    dp = [False for _ in range(len(p)+1)]
    dp[0] = True
    count = [0 for _ in range(len(p)+1)]
    count[0] = 1
    for i in range(0, len(p)+1):
        for j in range(i):
            if dp[j] is True and p[j:i] in towels:
                dp[i] = True
                count[i] += count[j]
    return count[len(p)]

part2()