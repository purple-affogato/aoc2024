filename = 'input/day17_input.txt'

def read_input():
    a, b, c = 0,0,0
    prg = []
    with open(filename) as f:
        for line in f:
            if "A" in line:
                a += int(line.removeprefix("Register A: ").strip())
            elif "B" in line:
                b += int(line.removeprefix("Register B: ").strip())
            elif "C" in line:
                c += int(line.removeprefix("Register C: ").strip())
            elif "P" in line:
                prg.extend(list(map(int, line.removeprefix("Program: ").strip().split(","))))
    return a,b,c,prg

def part1():
    a, b, c, prg = read_input()
    ptr = 0
    output = []
    # print(len(prg))
    while ptr < len(prg):
        opcode = prg[ptr]
        litop = prg[ptr+1]
        combo_op = litop
        if litop == 4:
            combo_op = a
        elif litop == 5:
            combo_op = b
        elif litop == 6:
            combo_op = c
        # print(opcode,litop)
        if opcode == 0:
            a = a >> combo_op
        elif opcode == 1:
            b = b ^ litop
        elif opcode == 2:
            b = combo_op % 8
        elif opcode == 3 and a != 0:
            ptr = litop
            continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo_op % 8)
            # print(bin(a%8),bin(b%8),bin(c%8))
        elif opcode == 6:
            b = a >> combo_op
        elif opcode == 7:
            c = a >> combo_op
        
        ptr += 2
    for i in range(len(output)):
        print(output[i], end="," if i < len(output)-1 else "\n")

ans2 = -1

def part2():
    global ans2
    a,b,c,prg = read_input()
    solve_p2(prg, len(prg)-1, 0)
    print(ans2)

def solve_p2(prg, i, ans):
    global ans2
    # print(ans, i)
    if i < 0:
        ans2 = min(ans2, ans) if ans2 > 0 else ans
    n = 0
    while n < 8:
        a2 = (ans<<3) + n
        # print((n ^ 6 ^ (a2 >> (n^3))) % 8)
        if prg[i] == (n ^ 6 ^ (a2 >> (n^3))) % 8:
            solve_p2(prg, i-1, (ans << 3) + n)
        n += 1
    return -1

# part1()
part2()