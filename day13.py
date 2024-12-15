import re

filename = "input/day13_input.txt"
A = []
B = []
prize = []

with open(filename) as f:
    idx = 0
    for line in f:
        if idx % 4 == 0: # button A
            vals = re.findall(r'(X\+(\d+))|(Y\+(\d+))', line)
            # print(vals)
            A.append((int(vals[0][1]), int(vals[1][3])))
        elif idx % 4 == 1: # button b
            vals = re.findall(r'(X\+(\d+))|(Y\+(\d+))', line)
            B.append((int(vals[0][1]), int(vals[1][3])))
        elif idx % 4 == 2:
            vals = re.findall(r'(X=(\d+))|(Y=(\d+))', line)
            # prize.append((int(vals[0][1]), int(vals[1][3])))
            prize.append((int(vals[0][1]) + 10000000000000, int(vals[1][3]) + 10000000000000)) # part 2
        idx += 1

def part1():
    global A
    global B
    global prize
    ans = 0
    for c in range(len(A)):
        min_price = 5000
        for i in range(0, 101):
            for j in range(0, 101):
                x = i * A[c][0] + j * B[c][0]
                y = i * A[c][1] + j * B[c][1]
                if x == prize[c][0] and y == prize[c][1]:
                    min_price = min(min_price, i * 3 + j)
        if min_price != 5000:
            ans += min_price
    print(ans)

min_tokens = 0
solved = False
def part2():
    global A
    global B
    global prize
    ans = 0
    
    for c in range(len(A)):
        if prize[c][0] % gcd(A[c][0], B[c][0]) > 0 or prize[c][1] % gcd(A[c][1], B[c][1]) > 0:
            continue
        dem = A[c][0] * B[c][1] - B[c][0] * A[c][1]
        x = (prize[c][0] * B[c][1] - prize[c][1] * B[c][0]) // dem
        y = (prize[c][1] * A[c][0] - prize[c][0] * A[c][1]) // dem
        if x >= 0 and y >= 0 and prize[c][0] == x * A[c][0] + y * B[c][0] and prize[c][1] == x * A[c][1] + y * B[c][1]:
            ans += 3*x + y
    print(ans)

def gcd(x:int, y:int):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

part2()
# print(gcd(432, 126))