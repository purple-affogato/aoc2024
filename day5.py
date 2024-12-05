from os import path
path.relpath

filename = path.realpath('input/day5_input.txt')
rules = {}
updates = []

with open(filename) as f:
    for line in f:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if x not in rules:
                rules[x] = []
            rules[x].append(y)
        elif "," in line:
            updates.append(list(map(int, line.strip().split(","))))

def part1():
    global rules
    global updates
    ans = 0
    for u in updates:
        prev = []
        correct = True
        for i in u:
            prev.append(i)
            if i not in rules:
                continue
            for j in rules[i]:
                if j in prev:
                    correct = False
                    break
        if correct:
            ans += u[len(u)//2]
            print(u, ans)
    print(ans)

def build_correct_order(u):
    global rules
    indeg = {}
    for i in u:
        indeg[i] = 0
    for i in u:
        if i not in rules:
            continue
        for j in rules[i]:
            if j in u:
                indeg[j] += 1
    q = []
    # print(indeg)
    for i in indeg.keys():
        if indeg[i] == 0:
            q.append(i)
    new_order = []
    while len(q) > 0:
        cur = q.pop(0)
        new_order.append(cur)
        if cur not in rules:
            continue
        for j in rules[cur]:
            if j not in u or j in new_order:
                continue
            indeg[j] = indeg[j] - 1
            if indeg[j] == 0:
                q.append(j)
    # print(new_order, u)
    if len(new_order) == 0:
        return 0
    return new_order[len(new_order)//2]

def part2():
    global rules
    global updates
    ans = 0
    for u in updates:
        correct = True
        swaps = []
        for i in range(len(u)):
            if u[i] not in rules:
                continue
            for j in rules[u[i]]: # j = nums that should be before u[i]
                for p in range(i):
                    if u[p] == j:
                        correct = False
        if not correct:
            # print(u)
            for (a, b) in swaps:
                u[a], u[b] = u[b], u[a]
            ans += build_correct_order(u)
            # print(u, ans)
    print(ans)

part2()