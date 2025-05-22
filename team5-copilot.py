from collections import deque

def digit_sum(n):
    # Returns the sum of the digits of the absolute value of n
    return sum(int(d) for d in str(abs(n)))

def isSafe(x, y):
    # Checks if the coordinate (x, y) is safe (digit sum of x*y < 19)
    product = x * y
    return digit_sum(product) < 19

def totalSafeSquares():
    # Returns the total number of safe squares reachable from (0, 0)
    visited = set()  # Set to keep track of visited coordinates
    queue = deque()
    queue.append((0, 0))  # Start from (0, 0)
    visited.add((0, 0))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy  # Calculate neighbor coordinates
            # If not visited and safe, add to queue and visited set
            if (nx, ny) not in visited and isSafe(nx, ny):
                visited.add((nx, ny))
                queue.append((nx, ny))
    return len(visited)  # Total number of reachable safe squares

def shortestSafeJourney(a, b, x, y):
    # Returns the shortest number of steps from (a, b) to (x, y) using only safe squares
    if not isSafe(a, b) or not isSafe(x, y):
        return -1  # If start or end is not safe, return -1
    visited = set()
    queue = deque()
    queue.append((a, b, 0))  # (current_x, current_y, steps)
    visited.add((a, b))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

    while queue:
        cx, cy, steps = queue.popleft()
        if (cx, cy) == (x, y):
            return steps  # Reached destination
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # If not visited and safe, add to queue and visited set
            if (nx, ny) not in visited and isSafe(nx, ny):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # No safe path found