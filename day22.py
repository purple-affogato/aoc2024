filename = "input/day22_input.txt"

def read_input()->list:
    nums = []
    with open(filename) as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums

def part1():
    nums = read_input()
    ans = 0
    for n in nums:
        for i in range(2000):
            n = prune(mix(n*64, n))
            n = prune(mix(n//32, n))
            n = prune(mix(n*2048, n))
        ans += n
        # print(n)
    print(ans)

def mix(x:int, secret:int)->int:
    return secret ^ x

def prune(secret:int)->int:
    return secret % 16777216

def part2():
    nums = read_input()
    diff = {}
    seq = {}
    for n in nums:
        cur = n
        prev = 0
        diff[n] = []
        seq[n] = []
        for i in range(2000):
            cur = prune(mix(cur*64, cur))
            cur = prune(mix(cur//32, cur))
            cur = prune(mix(cur*2048, cur))
            seq[n].append(cur%10)
            if i > 0:
                diff[n].append(cur%10-prev)
            prev = cur%10
    print("got sequences")
    # find sequence of 4 nums
    bananas = {}
    for k in diff.keys():
        prev = []
        for i in range(len(diff[k])-3):
            s = tuple(diff[k][i:i+4])
            if s not in bananas:
                bananas[s] = 0
            elif s in prev:
                continue
            bananas[s] += seq[k][i+4]
            prev.append(s)
    ans = -1
    for k in bananas.keys():
        ans = max(ans, bananas[k])
        # if bananas[k] > 20:
        #     print(k, bananas[k])
    print(ans)
         

part2()