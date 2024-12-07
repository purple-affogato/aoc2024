filename = 'input/day7_input.txt'
eqs = []

with open(filename) as f:
    for line in f:
        elts = line.strip().split()
        e = []
        e.append(int(elts[0][0:-1]))
        for i in range(1, len(elts)):
            e.append(int(elts[i]))
        eqs.append(e)

def valid(nums: list, target: int, idx: int, cur: int) -> bool:
    if idx == len(nums):
        return cur == target
    return valid(nums, target, idx+1, cur+nums[idx]) or valid(nums, target, idx+1, cur*nums[idx])

def part1(eqs: list):
    ans = 0
    for e in eqs:
        if valid(e[1:], e[0], 1, e[1]):
            ans += e[0]
    print(ans)

def valid2(nums: list, target: int, idx: int, cur: int) -> bool:
    if idx == len(nums):
        return cur == target
    elif cur > target:
        return False
    return valid2(nums, target, idx+1, cur+nums[idx]) or valid2(nums, target, idx+1, cur*nums[idx]) or valid2(nums, target, idx+1, cur*(10**len(str(nums[idx])))+nums[idx])

def part2(eqs: list):
    ans = 0
    for e in eqs:
        if valid2(e[1:], e[0], 1, e[1]):
            ans += e[0]
            # print(ans)
    print(ans)

part2(eqs)
