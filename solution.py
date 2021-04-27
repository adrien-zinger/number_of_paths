# Paths finding approach
def solution1():
    m, n = [int(input()), int(input())]
    t = (n - 1, m - 1)
    rows = [input() for _ in range(m)]
    v = 0
    queue=[(0,0)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        nx, ny = [x + 1, y + 1]
        if t in [(nx, y), (x, ny)]:
            v = v + 1;continue
        if nx < n and rows[y][nx] == '0':
            queue.append((nx, y))
        if ny < m and rows[ny][x] == '0':
            queue.append((x, ny))

    print(v)

# Dynamic approach
def solution2():
    m, n = [int(input()), int(input())]
    tb = [[0] * n for _ in range(m) ]
    tb[0][0] = 1
    for y in range(m):
        raw = [int(c) for c in input()]
        for x in range(n):
            if raw[x]: continue
            if y > 0:
                tb[y][x] += tb[y-1][x]
            if x > 0: 
                tb[y][x] += tb[y][x-1]
    print(tb[m-1][n-1])