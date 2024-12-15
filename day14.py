import time

filename = "input/day14_input.txt"
robots = []

with open(filename) as f:
    for line in f:
        p, v = line.split()
        p = p.removeprefix("p=")
        v = v.removeprefix("v=")
        p_vals = list(map(int, p.split(",")))
        v_vals = list(map(int, v.split(",")))
        robots.append((p_vals[0], p_vals[1], v_vals[0], v_vals[1]))

# print(robots)

def part1(robots: list):
    width = 101
    height = 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in robots:
        px, py = r[0] + r[2]*100, r[1] + r[3]*100
        # print(px, py)
        px = (px + width * 100) % width
        py = (py + height * 100) % height
        # print(px, py)
        if px < width // 2 and py < height // 2:
            q1 += 1
        elif px > width // 2 and py < height // 2:
            q2 += 1
        elif px < width // 2 and py > height // 2:
            q3 += 1
        elif px > width // 2 and py > height // 2:
            q4 += 1
    # print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)

def part2(robots:list):
    width = 101
    height = 103
    step = 1000
    while True:
        print("\n",step)
        matrix = [[0 for _ in range(width)] for _ in range(height)]
        valid = True
        for r in robots:
            px, py = r[0] + r[2]*step, r[1] + r[3]*step
            px = (px + width * step) % width
            py = (py + height * step) % height
            matrix[py][px] += 1
            if matrix[py][px] > 1:
                valid = False
                break
        if not valid:
            step += 1
            # time.sleep(0.5)
            continue
        for i in range(height):
            for j in range(width):
                p = " "
                if matrix[i][j] > 0:
                    p = str(matrix[i][j])
                print(p, end="")
            print("")
        step += 1
        time.sleep(5)

part2(robots)