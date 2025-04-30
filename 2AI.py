from collections import deque

def water_jug(j1, j2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        if a == target or b == target:
            print(f"Success: ({a}, {b})")
            return True
        queue.extend([
            (j1, b), (a, j2), (0, b), (a, 0),
            (a - min(a, j2 - b), b + min(a, j2 - b)),
            (a + min(b, j1 - a), b - min(b, j1 - a))
        ])
    print("No solution")
    return False

water_jug(4, 3, 2)
