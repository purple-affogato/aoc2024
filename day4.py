filename = 'input/day4_input.txt'
wordsearch = []
xmas = "XMAS"
cnt = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def search_xmas(i:int, j:int, l:int, d:int):
    global wordsearch
    global cnt
    if l == 4:
        cnt += 1
        return
    new_i = i + dirs[d][0]
    new_j = j + dirs[d][1]
    if 0 <= new_i < len(wordsearch) and 0 <= new_j < len(wordsearch[new_i]) and wordsearch[new_i][new_j] == xmas[l]:
        search_xmas(new_i, new_j, l+1, d)

def part1():
    global wordsearch
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'X':
                    for d in range(len(dirs)):
                        search_xmas(i, j, 1, d)

def search_x_mas(i:int, j:int):
    global wordsearch
    global cnt
    if wordsearch[i-1][j-1] == 'M' and wordsearch[i-1][j+1] == 'S' and wordsearch[i+1][j-1] == 'M' and wordsearch[i+1][j+1] == 'S':
        cnt += 1
    elif wordsearch[i-1][j-1] == 'S' and wordsearch[i-1][j+1] == 'S' and wordsearch[i+1][j-1] == 'M' and wordsearch[i+1][j+1] == 'M':
        cnt += 1
    elif wordsearch[i-1][j-1] == 'S' and wordsearch[i-1][j+1] == 'M' and wordsearch[i+1][j-1] == 'S' and wordsearch[i+1][j+1] == 'M':
        cnt += 1
    elif wordsearch[i-1][j-1] == 'M' and wordsearch[i-1][j+1] == 'M' and wordsearch[i+1][j-1] == 'S' and wordsearch[i+1][j+1] == 'S':
        cnt += 1

def part2():
    global wordsearch
    for i in range(1, len(wordsearch)-1):
        for j in range(1, len(wordsearch[i])-1):
            if wordsearch[i][j] == 'A':
                search_x_mas(i, j)

with open(filename) as f:
    for line in f:
        wordsearch.append(list(line.strip()))
# print(wordsearch)
part2()

print(cnt)