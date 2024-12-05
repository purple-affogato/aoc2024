cnt = 0
with open('input/day2_input.txt', 'r') as f:
    for line in f:
        lvls = list(map(int, line.split()))
        inc = True
        safe = True
        # determine inc or dec
        if lvls[0] > lvls[1]:
            inc = False
        elif lvls[0] == lvls[1]:
            continue
        # check difference before proceeding
        if abs(lvls[0] - lvls[1]) < 1 or abs(lvls[0] - lvls[1]) > 3:
            continue
        for i in range(1, len(lvls)-1):
            diff = abs(lvls[i+1] - lvls[i])
            if diff < 1 or diff > 3:
                safe = False
                break
            if inc and lvls[i] >= lvls[i+1]:
                    safe = False
                    break
            elif not inc and lvls[i] <= lvls[i+1]:
                safe = False
                break
        if safe:
            cnt += 1
print(cnt)
