from collections import deque

def valid(m1, c1, m2, c2):
    return all(x >= 0 and x <= 3 for x in [m1, c1, m2, c2]) and (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2)

def successors(state):
    m1, c1, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    res = []
    for m, c in moves:
        if boat == 0:
            new = (m1 - m, c1 - c, 1)
        else:
            new = (m1 + m, c1 + c, 0)
        m2, c2 = 3 - new[0], 3 - new[1]
        if valid(*new[:2], m2, c2):
            res.append(new)
    return res

def solve():
    start, goal = (3,3,0), (0,0,1)
    queue = deque([(start, [start])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for s in successors(state):
            if s not in seen:
                seen.add(s)
                queue.append((s, path + [s]))

for step in solve(): print(step)
