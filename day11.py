import math

filename = "input/day11_input.txt"
stones = []

with open(filename) as f:
    stones = list(map(int, f.read().split()))

def blink(x: list): # oh in a blink gone
    after = []
    for i in x:
        if i == 0:
            after.append(1)
        elif (int(math.log10(i)) + 1) % 2 == 0:
            p10 = 10**((int(math.log10(i)) + 1)/2)
            tmp = int(i // p10)
            after.append(tmp)
            after.append(i-tmp*p10)
            print(i, tmp)
        else:
            after.append(i*2024)
    return after

def part1(s: list):
    ans = 0
    for i in s:
        b = [i]
        for _ in range(25):
            b = blink(b)
        ans += len(b)
    print(ans)

cnt = {}

def solve(x: int, blinks: int) -> int:
    global cnt
    if x not in cnt:
        cnt[x] = {}
    # base cases
    if blinks == 0:
        cnt[x][0] = 1
        return cnt[x][0]
    if x in cnt:
        if blinks in cnt[x]:
            return cnt[x][blinks]
    # recursion
    if x == 0:
        cnt[x][blinks] = solve(1, blinks-1)
    elif (int(math.log10(x)) + 1) % 2 == 0:
        sx = str(x)
        cnt[x][blinks] = solve(int(sx[:len(sx)//2]), blinks-1) + solve(int(sx[len(sx)//2:]), blinks-1)
    else:
        cnt[x][blinks] = solve(x*2024, blinks-1)
    return cnt[x][blinks]

def part2(s: list):
    global cnt
    ans = 0
    for i in s:
        ans += solve(i, 75)
    print("stones?",ans)

part2(stones)
