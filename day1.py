l = []
r = []
freq = {}
with open('input/day1_input.txt', 'r') as f:
    for line in f:
        a, b = map(int, line.split())
        freq[b] = freq.get(b, 0) + 1
        l.append(a)
        r.append(b)
ans = 0
for i in l:
    ans += i * freq.get(i, 0)
print(ans)
