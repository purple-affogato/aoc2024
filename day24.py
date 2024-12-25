filename = 'input/day24_input_og.txt'

def read_input():
    vals = {}
    ops = []
    x, y = 0, 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            elif "->" in line:
                l = line.split()
                ops.append(l)
                # print(l[0], l[-1])
                # print(l[2], l[-1])
            elif line[0] == 'x' or line[0] == 'y':
                l = line.split(": ")
                vals[l[0]] = int(l[1])
                if line[0] == 'x':
                    x += int(l[1]) << int(l[0][1:])
                else:
                    y += int(l[1]) << int(l[0][1:])
    # print(x+y, bin(x+y))
    with open("test.gv", "w") as f:
        f.write("digraph G {\n")
        for o in ops:
            f.write("\t"+o[0]+" -> "+o[-1]+" [xlabel=" + o[1] + "];\n")
            f.write("\t"+o[2]+" -> "+o[-1] + ";\n")
        f.write("}")
    return vals, ops, x+y

def part1(vals:dict, ops:list, z:int):
    global w, edges
    symbol = {"AND":"&", "OR":"|", "XOR":"^"}
    max_z = 0
    while len(ops) > 0:
        for o in ops:
            if o[0] in vals and o[2] in vals:
                vals[o[-1]] = operation(o[1], vals[o[0]], vals[o[2]])
                if o[-1][0] == 'z':
                    max_z = max(max_z, int(o[-1][1:]))
                ops.remove(o)
    ans = 0
    for i in range(max_z+1):
        v = 'z' + (str(i) if i > 9 else ('0' + str(i)))
        ans += vals[v] << i
        # print(v, vals[v])
        if vals[v] != (z >> i) & 1:
            print(i)
    print(bin(ans))
    print(bin(z))
    return ans == z

def part2():
    vals, ops, z = read_input()
    gates = {}
    carry = "jwf"
    xor_gates = {}
    and_gates = {}
    for o in ops:
        if o[0][0] == 'x' or o[0][0] == 'y':
            if o[1] == "XOR":
                xor_gates[int(o[0][1:])] = o[-1]
            elif o[1] == "AND":
                and_gates[int(o[0][1:])] = o[-1]
        else:
            if o[0] not in gates:
                gates[o[0]] = {}
            if o[2] not in gates:
                gates[o[2]] = {}
            gates[o[0]][o[1]] = (o[2], o[-1])
            gates[o[2]][o[1]] = (o[0], o[-1])

    for bit in range(2, 45):
        x1, a1 = xor_gates[bit], and_gates[bit]
        if x1[0] == 'z' or a1[0] == 'z':
            print(bit)
        elif gates[x1]["XOR"][0] != carry:
            print(bit, gates[x1]["XOR"][0])
        elif gates[x1]["XOR"][1][0] != 'z':
            print(bit)
        elif gates[x1]["AND"][1] != gates[carry]["AND"][1]:
            print(bit)
        a1 = gates[gates[carry]["AND"][1]]["OR"][0]
        x1 = gates[carry]["XOR"][0]
        carry = gates[a1]["OR"][1]

def operation(gate:str, x:int, y:int)->int:
    match gate:
        case "AND":
            return x & y
        case "OR":
            return x | y
        case "XOR":
            return x ^ y
        case _:
            return -1

# vals, ops, z = read_input()
# print(part1(vals, ops, z))
part2()