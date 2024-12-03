def pd(a, idx:int) -> bool:
    a.pop(idx)
    inc = True
    # determine inc or dec
    if a[0] > a[1]:
        inc = False
    elif a[0] == a[1]:
        return False
    # check difference before proceeding
    if abs(a[0] - a[1]) < 1 or abs(a[0] - a[1]) > 3:
        return False
    for i in range(1, len(a)-1):
        diff = abs(a[i+1] - a[i])
        if diff < 1 or diff > 3:
            return False
        if inc and a[i] >= a[i+1]:
            return False
        elif not inc and a[i] <= a[i+1]:
            return False
    return True

cnt = 0
with open('day2_input.txt', 'r') as f:
    for line in f:
        lvls = list(map(int, line.split()))
        inc = True
        safe = True
        if pd(lvls.copy(), 0):
            cnt += 1
            continue
        # check difference before proceeding
        if abs(lvls[0] - lvls[1]) < 1 or abs(lvls[0] - lvls[1]) > 3 or lvls[0] == lvls[1]:
            if pd(lvls.copy(), 0) or pd(lvls.copy(), 1):
                cnt += 1
                continue
        # determine inc or dec
        if lvls[0] > lvls[1]:
            inc = False
        for i in range(1, len(lvls)-1):
            diff = abs(lvls[i+1] - lvls[i])
            if diff < 1 or diff > 3:
                if pd(lvls.copy(), i) or pd(lvls.copy(), i+1):
                    safe = True
                else:
                    safe = False
                break
            if inc and lvls[i] >= lvls[i+1]:
                if pd(lvls.copy(), i) or pd(lvls.copy(), i+1):
                    safe = True
                else:
                    safe = False
                break

            elif not inc and lvls[i] <= lvls[i+1]:
                if pd(lvls.copy(), i) or pd(lvls.copy(), i+1):
                    safe = True
                else:
                    safe = False
                break
        if safe:
            cnt += 1
print(cnt)
