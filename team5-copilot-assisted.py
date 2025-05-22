from collections import deque

def digit_sum(n):
    # Returns the sum of the digits of the absolute value of n
    return sum(int(d) for d in str(abs(n)))

def isSafe(x, y):
    # Checks if the coordinate (x, y) is safe (digit sum of x*y < 19)
    product = x * y
    return digit_sum(product) < 19

def totalSafeSquares(max_dist=9999):
    # Returns the total number of safe squares reachable from (0, 0) within max_dist
    visited = set()           # Set to keep track of visited coordinates
    queue = deque()           # Queue for BFS
    queue.append((0, 0))      # Start from (0, 0)
    visited.add((0, 0))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

    while queue:
        cx, cy = queue.popleft()  # Get the next coordinate to explore
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy  # Calculate neighbor coordinates
            # Limit the search to within max_dist from (0,0)
            if abs(nx) > max_dist or abs(ny) > max_dist:
                continue
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
        cx, cy, steps = queue.popleft()  # Get the next coordinate and step count
        if (cx, cy) == (x, y):
            return steps  # Reached destination
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # If not visited and safe, add to queue and visited set
            if (nx, ny) not in visited and isSafe(nx, ny):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # No safe path found

if __name__ == "__main__":
    # This block runs only if the script is executed directly (not imported as a module)
    
    # Print the number of safe squares reachable from (0, 0)
    # The max_dist parameter limits how far from (0, 0) the search will go
    print("Number of safe squares:", totalSafeSquares(9999))  # 9999 is adjustable
    
    # Print the shortest number of steps in a safe journey from (0,0) to (5,5)
    # Returns -1 if there is no safe path
    print("Shortest safe journey from (0,0) to (5,5):", shortestSafeJourney(0, 0, 5, 5))