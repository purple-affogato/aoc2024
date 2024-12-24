filename = "input/day23_input.txt"

def read_input()->list:
    edges = []
    with open(filename) as f:
        for line in f:
            a, b = map(str, line.strip().split("-"))
            edges.append((a, b))
    return edges

def part1():
    edges = read_input()
    adj = {}
    comps = []
    for e in edges:
        if e[0] not in adj:
            adj[e[0]] = []
            comps.append(e[0])
        if e[1] not in adj:
            adj[e[1]] = []
            comps.append(e[1])
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    ans = set()
    for c in comps:
        for i in range(len(adj[c])):
            for j in range(i+1, len(adj[c])):
                a, b = adj[c][i], adj[c][j]
                if c[0] != 't' and a[0] != 't' and b[0] != 't':
                    continue
                if b not in adj[a]:
                    continue
                s = tuple(sorted([c, a, b]))
                # print(s)
                ans.add(s)
    print(len(ans))
    # print(ans)

ans2 = []

def part2():
    global ans2
    edges = read_input()
    adj = {}
    comps = []
    for e in edges:
        if e[0] not in adj:
            adj[e[0]] = []
            comps.append(e[0])
        if e[1] not in adj:
            adj[e[1]] = []
            comps.append(e[1])
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    comps.sort()
    # print(comps)
    find_lan_party(comps, adj, 0, [])
    for a in ans2:
        print(a, end="," if a != ans2[-1] else "\n")

def find_lan_party(comps:list, adj:dict, idx:int, party:list):
    global ans2
    if len(party) >= len(ans2):
        ans2 = party.copy()
    for i in range(idx, len(comps)):
        add = True
        for p in party:
            if comps[i] not in adj[p]:
                add = False
                break
        if add is False:
            continue
        party.append(comps[i])
        find_lan_party(comps, adj, i+1, party)
        party.pop()
    # find_lan_party(comps, adj, idx+1, party)


part2()